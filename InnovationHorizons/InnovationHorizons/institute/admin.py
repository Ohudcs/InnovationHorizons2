from django.contrib import admin
from .models import Admin,  Teacher, Lesson, Grade, Assignment, Attendance, Student

# Register your models here.
admin.site.register(Admin)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Assignment)
admin.site.register(Attendance)
admin.site.register(Student)
