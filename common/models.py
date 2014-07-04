from django.db import models
from teachers.models import Teacher


class Area(models.Model):
    area_name = models.CharField()

    def __str__(self):
        return self.area_name


class Building(models.Model):
    building_name = models.CharField()
    area = models.ForeignKey('Area')

    def __str__(self):
        return self.building_name


class Room(models.Model):
    room_name = models.CharField()
    building = models.ForeignKey('Building')

    def __str__(self):
        return self.room_name


class Course(models.Model):
    course_id = models.CharField()
    course_seq = models.CharField()
    course_name = models.CharField()
    course_mark = models.DecimalField()
    course_attr = models.CharField()
    examine_manner = models.CharField()

    def __str__(self):
        return self.course_name


class CourseInstance(models.Model):
    course = models.ForeignKey('Course')
    teacher = models.ForeignKey('Teacher')
    exam_prop = models.CharField()
    is_postponed = models.BooleanField()


class RoomTaken(models.Model):
    room = models.ForeignKey('Room')
    course_instance = models.ForeignKey('CourseInstance')
    start_week = models.PositiveIntegerField()
    end_week = models.PositiveIntegerField()
    week_day = models.PositiveIntegerField()
    section = models.PositiveIntegerField()