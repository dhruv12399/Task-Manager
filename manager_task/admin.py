from __future__ import unicode_literals

from django.contrib import admin

from .models import Task, Activity

# Register your models here.

admin.site.register(Activity)

admin.site.register(Task)