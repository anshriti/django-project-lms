from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from core.models import Teacher ,Student, Assignment,material
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'
    paginate_by = 5

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index') 

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(DeleteView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_delete_confirm.html'
    success_url = reverse_lazy('teacher.index')

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_index.html'
    context_object_name = 'students'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
    template_name = 'students/student_form.html'
    success_url = 'student.index' 
