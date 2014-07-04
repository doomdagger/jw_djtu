from django.db import models
from common.models import CourseInstance


# student model
class Student(models.Model):
    username = models.CharField()
    password = models.CharField()
    real_name = models.CharField()
    academy = models.CharField()
    major = models.CharField()
    dedication = models.CharField()
    student_category = models.CharField()
    enroll_grade = models.PositiveIntegerField()
    class_name = models.CharField()
    cert_category = models.CharField()
    cert_id = models.CharField()
    email = models.EmailField()
    phone_number = models.CharField()
    address = models.CharField()
    postcode = models.CharField()

    def __str__(self):
        return self.real_name


# award record model
class AwardRecord(models.Model):
    student = models.ForeignKey('Student')
    award_category = models.CharField()
    award_date = models.DateField()
    award_name = models.CharField()
    award_remark = models.CharField()


class StudentCourse(models.Model):
    course_instance = models.ForeignKey('CourseInstance')
    student = models.ForeignKey('Student')
    school_year = models.PositiveIntegerField()
    school_term = models.PositiveIntegerField()
    normal_score = models.FloatField()
    final_score = models.FloatField()
    eval_score = models.FloatField()
    is_postponed = models.BooleanField()
    remark = models.CharField()