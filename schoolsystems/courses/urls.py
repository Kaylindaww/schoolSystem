from io import StringIO
from  django.urls import path
from .views import register_courses, register_courses
from.views import register_courses


urlpatterns=[
    path("register/", register_courses, name="register_courses"),
    path("list/",register_courses,name="course_list"),
]