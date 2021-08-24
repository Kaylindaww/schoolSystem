from  django.urls import path
from .views import register_events
from.views import register_events


urlpatterns=[
    path("register/", register_events, name="register_events"),
    path("list/",register_events,name="events_list"),
]
