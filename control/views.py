from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from djitellopy import Tello
import cv2
import time


tello = Tello()


def takeoff(request):
    print("taking off")

    tello.takeoff()
    battery = tello.get_battery()
    print(battery)
    return HttpResponseRedirect("/control")


def land(request):
    print("landing")
    tello.land()
    return HttpResponseRedirect("/control")


def forward(request):
    print("forward")
    tello.move_forward(30)
    return HttpResponseRedirect("/control")


def backward(request):
    print("backward")
    tello.move_back(30)
    return HttpResponseRedirect("/control")


def left(request):
    print("left")
    tello.move_left(30)
    return HttpResponseRedirect("/control")


def right(request):
    print("right")
    tello.move_right(30)
    return HttpResponseRedirect("/control")


def turn_left(request):
    tello.rotate_counter_clockwise(90)
    return HttpResponseRedirect("/control")


def turn_right(request):
    tello.rotate_clockwise(90)
    return HttpResponseRedirect("/control")


def picture(request):
    tello.streamon()
    frame_read = tello.get_frame_read()
    cv2.imwrite("picture.png", frame_read.frame)  # type:ignore
    response = FileResponse(open("picture.png", "rb"), as_attachment=True)
    return response


def show(request):
    tello.takeoff()
    time.sleep(1)
    tello.land()
    return HttpResponseRedirect("/control")


def emergency_stop(request):
    tello.emergency()
    return HttpResponseRedirect("/control")


def flip_forward(request):
    # need to be tested in large area , no idea about it's behavior
    tello.flip_forward()
    return HttpResponseRedirect("/control")


def flip_backward(request):
    tello.flip_back()
    return HttpResponseRedirect("/control")


def index(request):
    try:
        tello.connect(wait_for_state=False)
        battery = tello.get_battery()
        # TODO: stay connected after drone if off, need server restart
        return render(
            request,
            "control/index.html",
            context={"connected": True, "battery": battery},
        )
    except:
        return render(
            request, "control/index.html", context={"connected": False, "battery": 0}
        )
