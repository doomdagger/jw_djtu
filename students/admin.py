from django.contrib import admin
from students import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)