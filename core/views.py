from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.models import Teacher, Student, Assignment, Material
from django.urls import reverse_lazy
from core.forms import TeacherForm, AssignmentForm
from django.contrib.auth.mixins import LoginRequiredMixin #class base view
from django.contrib.auth.decorators import login_required  #function base view

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# Teacher Views
class TeacherListView(LoginRequiredMixin,ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = context['page_obj']  # Now 'teachers' is the Page object
        return context

class TeacherCreateView(LoginRequiredMixin,CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')

class TeacherDetailView(LoginRequiredMixin,DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(LoginRequiredMixin,DeleteView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_delete_confirm.html'
    success_url = reverse_lazy('teacher.index')

# Student Views
class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'students/student_index.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = context['page_obj']  # Now 'students ' is the Page object
        return context

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student.index')

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
    success_url = reverse_lazy('student.index')

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_delete_confirm.html'
    success_url = reverse_lazy('student.index')

class AssignmentListView(LoginRequiredMixin,ListView):
    model = Assignment
    template_name = 'assignments/assignment_index.html'
    context_object_name = 'assignments'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = context['page_obj']  # Now 'teachers' is the Page object
        return context

class AssignmentCreateView(LoginRequiredMixin,CreateView):
    model = Assignment
    form_class = AssignmentForm
    #fields = ['title', 'start_date', 'question_file','end_date', 'full_mark', 'subject','question', 'remark', 'teacher']
    template_name = 'assignments/assignment_form.html'
    success_url = reverse_lazy('assignment.index')

class AssignmentDetailView(LoginRequiredMixin,DetailView):
    model = Assignment
    template_name = 'assignments/assignment_detail.html'
    context_object_name = 'assignment'

class AssignmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignments/assignment_form.html'
    #fields = ['title', 'start_date', 'question_file','end_date', 'full_mark', 'subject','question', 'remark', 'teacher']
    success_url = reverse_lazy('assignment.index')

class AssignmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Assignment
    context_object_name = 'assignment'
    template_name = 'assignments/assignment_delete_confirm.html'
    success_url = reverse_lazy('assignment.index')