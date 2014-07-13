from django.db import models


class Area(models.Model):
    area_name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.area_name


class Building(models.Model):
    building_name = models.CharField(max_length=20, null=False, blank=False)
    area = models.ForeignKey('Area')

    def __str__(self):
        return self.building_name


class Room(models.Model):
    room_name = models.CharField(max_length=20, null=False, blank=False)
    building = models.ForeignKey('Building')

    def __str__(self):
        return self.room_name


class Course(models.Model):
    course_id = models.CharField(max_length=25, null=False, blank=False)
    course_name = models.CharField(max_length=50, null=False, blank=False)
    course_mark = models.DecimalField(max_digits=5, decimal_places=2)
    course_attr = models.CharField(max_length=20, null=False, blank=False, choices=(
        ('cmp', '必修'),
        ('limit', '限选'),
        ('opt', '任选')
    ))

    def __str__(self):
        return self.course_name


class CourseInstance(models.Model):
    course = models.ForeignKey('Course')
    teacher = models.ForeignKey('Teacher')
    course_seq = models.CharField(max_length=5, null=False, blank=False)
    is_postponed = models.BooleanField(null=False)
    school_year = models.PositiveIntegerField(null=False)
    examine_manner = models.CharField(max_length=20, null=False, blank=False, choices=(
        ('uncertain', '未确定'),
        ('certain', '确定')
    ))
    exam_prop = models.CharField(max_length=20, null=False, blank=False, choices=(
        ('normal', "正常考试"),
        ('postponed', "补缓考试"),
        ('recap', "重修考试")
    ))
    school_term = models.PositiveIntegerField(null=False, choices=(
        (1, '春'),
        (2, '秋')
    ))
    has_room = models.BooleanField()
    exam_date = models.DateTimeField(null=True)
    exam_last_minutes = models.PositiveIntegerField(null=True)
    exam_room = models.ForeignKey('Room', null=True)

    def __str__(self):
        return self.course.course_name + ":" + self.teacher.full_name


class RoomTaken(models.Model):
    room = models.ForeignKey('Room')
    course_instance = models.ForeignKey('CourseInstance')
    start_week = models.PositiveIntegerField()
    end_week = models.PositiveIntegerField()
    week_day = models.PositiveIntegerField()
    start_section = models.PositiveIntegerField()
    end_section = models.PositiveIntegerField()

    def __str__(self):
        return self.course_instance.course.course_name + ":" + self.room.room_name


class Teacher(models.Model):
    full_name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.full_name


# student model
class Student(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    real_name = models.CharField(max_length=20, null=False, blank=False)
    academy = models.CharField(max_length=50, null=False, blank=False)
    major = models.CharField(max_length=50, null=False, blank=False)
    dedication = models.CharField(max_length=100, null=False, blank=False)
    student_category = models.CharField(max_length=100, null=False, blank=False)
    enroll_grade = models.PositiveIntegerField(null=False)
    class_name = models.CharField(max_length=100, null=False, blank=False)
    cert_category = models.CharField(max_length=100, null=False, blank=False)
    cert_id = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    avatar = models.FileField(upload_to='avatar')

    def __str__(self):
        return self.real_name


# award record model
class AwardRecord(models.Model):
    student = models.ForeignKey('Student')
    award_category = models.CharField(max_length=100)
    award_date = models.DateField(auto_now=True, auto_now_add=True)
    award_name = models.CharField(max_length=100)
    award_remark = models.CharField(max_length=100)

    def __str__(self):
        return self.award_name


class StudentCourse(models.Model):
    course_instance = models.ForeignKey('CourseInstance')
    student = models.ForeignKey('Student')
    is_score_out = models.BooleanField()
    normal_score = models.FloatField(null=True)
    final_score = models.FloatField(null=True)
    eval_score = models.FloatField(null=True)
    is_postponed = models.BooleanField()
    remark = models.CharField(max_length=100, null=True, default="无")

    def __str__(self):
        return self.course_instance.course.course_name + ":" + self.student.real_name


class Announcement(models.Model):
    content = models.CharField(max_length=2000, null=False, blank=False)
    start_week = models.PositiveIntegerField()
    end_week = models.PositiveIntegerField()
    title = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.title


class Setting(models.Model):
    key = models.CharField(max_length=300, null=False, blank=False)
    value = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.key + ":" + self.value