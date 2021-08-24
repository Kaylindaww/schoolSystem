# Create your views here.
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Students


def register_trainer(request):
    form=StudentRegistrationForm()
    return render(request,'register_trainer.html', {'form':form})

def register_trainer(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_trainer.html",{'form':form}) 

def  trainer_list(request):
     student=Students.objects.all()
     return render(request,"trainer_list.html",{
         "students": student
     } )
     register_trainer,trainer_list
     path       
