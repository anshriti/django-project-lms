from django.contrib import admin
from core.models import Student, Teacher,Assignment,material
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(material)
