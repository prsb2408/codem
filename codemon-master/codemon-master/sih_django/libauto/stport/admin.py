from django.contrib import admin

# Register your models here.
from stport.models import student_info,login_info
admin.site.register(student_info)
admin.site.register(login_info)
