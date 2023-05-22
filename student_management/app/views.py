from django.shortcuts import render
from .models import Student
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm
# Create your views here.

def index(requset):
    return render(requset,'students/index.html',{
        'students': Student.objects.all()
    })
    
def view_student(requset,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(requset):
    if requset.method == 'POST':
        form = StudentForm(requset.POST)
        if form.is_valid():
            new_student_id = form.cleaned_data['student_id']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_filed_of_study = form.cleaned_data['field_of_study']
            new_gpa= form.cleaned_data['gpa']
            
            new_student = Student(
                student_id = new_student_id,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_filed_of_study,
                gpa = new_gpa                
            )
            
            new_student.save()
            return render(requset,'students/add.html',{
                'from' : StudentForm(),
                'success' : True
            })
    else:
        form = StudentForm()
    return render(requset,'students/add.html',{
            'form' : StudentForm()
    })
    
        
def edit(requset,id):
    if requset.method == 'POST':
        student= Student.objects.get(pk=id)
        form = StudentForm(requset.POST,instance=student)
        if form.is_valid():
            form.save()
            return render (requset,'students/edit.html', {
                'form' : form,
                'success' : True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)   
    return render (requset,'students/edit.html', {
                'form' : form
    })
    

def delete(requset,id):
    if requset.method == 'POST':
        student= Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))