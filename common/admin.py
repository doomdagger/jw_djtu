from django.contrib import admin
from common import models

# Register your models here.
admin.site.register(models.CourseInstance)
admin.site.register(models.Course)
admin.site.register(models.Area)
admin.site.register(models.Building)
admin.site.register(models.Room)
admin.site.register(models.RoomTaken)
admin.site.register(models.Teacher)
admin.site.register(models.AwardRecord)
admin.site.register(models.Student)
admin.site.register(models.StudentCourse)
admin.site.register(models.Announcement)
admin.site.register(models.Setting)