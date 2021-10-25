from django.shortcuts import render
from adminapp.models import *

# Create your views here.


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def editprofile(request):
    profile_obj = personaldetail.objects.all()
    print(profile_obj)
    return render(request, 'editprofile.html')


def leave(request):
    return render(request, 'leaveapplication.html')


def applyleave(request):
    leave_obje = leavetype.objects.all()
    return render(request, 'applyleave.html', {'leave': leave_obje})


def notification(request):
    return render(request, 'notification.html')


def leavedetail(request):
    return render(request, 'leavedetail.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def settings(request):
    return render(request, 'settings.html')


def attendance(request):
    return render(request, 'attendance.html')


def holiday(request):
    return render(request, 'holidaylist.html')
