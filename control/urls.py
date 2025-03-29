from django.urls import path
from control import views

app_name = "control"
urlpatterns = [
    path("", views.index, name="index"),
    path("takeoff/", views.takeoff, name="takeoff"),
    path("land/", views.land, name="land"),
    path("forward/", views.forward, name="forward"),
    path("backward/", views.backward, name="backward"),
    path("left/", views.left, name="left"),
    path("right/", views.right, name="right"),
    path("turn_left/", views.turn_left, name="turn_left"),
    path("turn_right/", views.turn_right, name="turn_right"),
    path("picture/", views.picture, name="picture"),
    path("emergency_stop/", views.emergency_stop, name="emergency_stop"),
    path("show/", views.show, name="show"),
]
