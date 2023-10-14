from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from app.forms import * 
# Create your views here.

from django.views.generic import View,TemplateView,FormView,ListView,DetailView,CreateView,UpdateView,DeleteView

class Home(View):
    def get(self,request):
        return render(request,'app/home.html')

class Temp_Context(TemplateView):
    template_name = 'app/Temp_Context.html'

    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['Name']='Satish'
        return ECDO

class Temp_Form(TemplateView):
    template_name = 'app/Temp_Form.html'

    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO

    def post(self,request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('<center><h1 style="color: green;">Data submitted successfully</h1></center>')

class Temp_FormView(FormView):
    form_class = SchoolForm
    template_name = 'app/Temp_FormView.html'

    def form_valid(self,form):
        form.save()
        return HttpResponse('<center><h1 style="color: green;">Data submitted successfully</h1></center>')

class School_ListView(ListView):
    model = School
    queryset = School.objects.order_by('Sname')
    template_name='app/School_ListView.html'
    context_object_name = 'SCO'
    # ordering = ['Sprincipal']


class School_Detail(DetailView):
    model = School
    context_object_name = 'School'

class School_CreateView(CreateView):
    model = School
    fields = '__all__'

class Student_ListView(ListView):
    model = Student
    context_object_name = 'STO'
    template_name='app/Student_List.html'

class Student_CreateView(CreateView):
    model = Student
    fields = '__all__'

class Student_Detail(DetailView):
    model = Student
    context_object_name = 'Student'


class School_UpdateView(UpdateView):
    model = School
    fields = '__all__'

class School_DeleteView(DeleteView):
    model = School
    context_object_name = 'Sc_Del'
    success_url = reverse_lazy('School_ListView')
