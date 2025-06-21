from rest_framework import serializers
from core.models import Teacher, Student
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields =  ['full_name', 'email', 'phone_no', 'department', 'join_date', 'user']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
        

