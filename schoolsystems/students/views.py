from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Students


def register_student(request):
    form=StudentRegistrationForm()
    return render(request,'register_student.html', {'form':form})

def register_student(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{'form':form}) 

def  Student_list(request):
     students=Students.objects.all()
     return render(request,"student_list.html",{
         "students": students
     } )
     register_student,Student_list
     path       