# Create your views here.
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Students


def register_courses(request):
    form=StudentRegistrationForm()
    return render(request,'register_courses.html', {'form':form})

def register_student(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_courses.html",{'form':form}) 

def  Student_list(request):
     student=Students.objects.all()
     return render(request,"student_courses.html",{
         "students": student
     } )
     register_courses,Student_courses
     path 
           