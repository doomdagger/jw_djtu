from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.db.models.query import exceptions
from django.http import HttpResponse
from django.template import RequestContext, loader

from common.models import Student


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
        elif error_code =='2':
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