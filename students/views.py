from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.db.models.query import exceptions
from django.http import HttpResponse
from django.template import RequestContext, loader

from common.models import Student
from common.models import StudentCourse
from common.models import RoomTaken
from common.models import Setting


def map_course_attr(course_attr):
    attr_map = {
        'cmp': '必修',
        'limit': '限选',
        'opt': '任选'
    }

    return attr_map[course_attr]


def map_examine_manner(examine_manner):
    manner_map = {
        'uncertain': '未确定',
        'certain': '确定'
    }
    return manner_map[examine_manner]


def map_exam_prop(exam_prop):
    prop_map = {
        'normal': "正常考试",
        'postponed': "补缓考试",
        'recap': "重修考试"
    }
    return prop_map[exam_prop]


# Create your views here.
def student_index(request):
    return render_to_response('index.html')


def student_signin(request):
    global message, message_type
    try:
        error_code = request.GET['error']

        if error_code == '0':
            message_type = 0
            message = '您已成功退出登陆'
        elif error_code == '1':
            message_type = 1
            message = '请输入学号与密码登陆教育系统'
        elif error_code == '2':
            message_type = 2
            message = '您输入的学号与密码不正确'
    except KeyError:
        message = ''
        message_type = -1

    template = loader.get_template('signin.html')
    context = RequestContext(request, {
        'message': message,
        'message_type': message_type
    })
    return HttpResponse(template.render(context))


def student_dosignin(request):

    try:
        username = request.POST['username']
        password = request.POST['password']

        user = Student.objects.get(username=username, password=password)

        request.session['signin_status'] = True
        request.session['signin_username'] = user.username
        request.session['signin_id'] = user.id

        redirect_url = '/'

    except KeyError:
        redirect_url = '/signin/?error=1'
    except exceptions.ObjectDoesNotExist:
        redirect_url = '/signin/?error=2'

    return redirect(redirect_url)


def student_signout(request):

    request.session['signin_status'] = False
    request.session['signin_username'] = None
    request.session['signin_id'] = None

    return redirect('/signin/?error=0')


def student_change_password(request):

    return render_to_response('students/change_password.html')


def student_query_course(request):
    courses = []

    global year, term

    try:
        year = request.POST["school_year"]
        term = request.POST["school_term"]
    except KeyError:
        year = Setting.objects.get(key="school_year").value
        term = Setting.objects.get(key="school_term").value

    try:
        raw_courses = StudentCourse.objects.filter(student_id=request.session['signin_id'],
                                                   course_instance__school_year=int(year),
                                                   course_instance__school_term=int(term))
        for raw_course in raw_courses:
            temp_map = {"course_id": raw_course.course_instance.course.course_id,
                        "course_seq": raw_course.course_instance.course_seq,
                        "course_name": raw_course.course_instance.course.course_name,
                        "teacher": raw_course.course_instance.teacher,
                        "course_mark": raw_course.course_instance.course.course_mark,
                        "course_attr": map_course_attr(raw_course.course_instance.course.course_attr),
                        "examine_manner": map_examine_manner(raw_course.course_instance.examine_manner),
                        "exam_prop": map_exam_prop(raw_course.course_instance.exam_prop),
                        "is_postponed": raw_course.course_instance.is_postponed}
            raw_room_takens = RoomTaken.objects.filter(course_instance__id=raw_course.course_instance.id)
            temp_map["room_takens"] = []
            for raw_room_taken in raw_room_takens:
                temp_map["room_takens"].append({
                    "start_week": raw_room_taken.start_week,
                    "end_week": raw_room_taken.end_week,
                    "week_day": raw_room_taken.week_day,
                    "room_name": raw_room_taken.room.room_name,
                    "start_section": raw_room_taken.start_section,
                    "end_section": raw_room_taken.end_section
                })
            courses.append(temp_map)

    except exceptions.ObjectDoesNotExist:
            pass

    template = loader.get_template('students/query_course.html')
    context = RequestContext(request, {
        'courses': courses,
        'year': year,
        'term': term
    })
    return HttpResponse(template.render(context))


def student_query_score(request):
    scores = []

    global year, term

    try:
        year = request.POST["school_year"]
        term = request.POST["school_term"]
    except KeyError:
        year = Setting.objects.get(key="school_year").value
        term = Setting.objects.get(key="school_term").value

    try:
        raw_courses = StudentCourse.objects.filter(student_id=request.session['signin_id'],
                                                   course_instance__school_year=int(year),
                                                   course_instance__school_term=int(term),
                                                   is_score_out=True)

        for raw_course in raw_courses:
            temp_map = {"course_id": raw_course.course_instance.course.course_id,
                        "course_seq": raw_course.course_instance.course_seq,
                        "course_name": raw_course.course_instance.course.course_name,
                        "teacher": raw_course.course_instance.teacher,
                        "course_mark": raw_course.course_instance.course.course_mark,
                        "course_attr": map_course_attr(raw_course.course_instance.course.course_attr),
                        "exam_prop": map_exam_prop(raw_course.course_instance.exam_prop),
                        "is_postponed": raw_course.is_postponed,
                        "normal_score": raw_course.normal_score,
                        "final_score": raw_course.final_score,
                        "eval_score": raw_course.eval_score,
                        "remark": raw_course.remark
            }

            scores.append(temp_map)

    except exceptions.ObjectDoesNotExist:
            pass

    template = loader.get_template('students/query_score.html')
    context = RequestContext(request, {
        'scores': scores,
        'year': year,
        'term': term
    })
    return HttpResponse(template.render(context))