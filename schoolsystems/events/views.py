from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Students


def register_events(request):
    form=StudentRegistrationForm()
    return render(request,'register_events.html', {'form':form})

def register_events(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_events.html",{'form':form}) 

def  register_events(request):
     student=Students.objects.all()
     return render(request,"events_list.html",{
         "students": student
     } )
     register_events,events_list
     path       
