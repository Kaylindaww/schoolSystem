from  django.urls import path
from .views import register_student
from.views import register_student,Student_list


urlpatterns=[
    path("register/", register_student, name="register_student"),
    path("list/",Student_list,name="student_list"),
]
