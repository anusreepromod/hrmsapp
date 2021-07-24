from django.shortcuts import render

# Create your views here.


def employee(request):
    return render(request, 'employee.html')


def addstaff(request):
    return render(request, 'addstaff.html')


def editemployee(request):
    return render(request, 'editemployee.html')


def manageleave(request):
    return render(request, 'manageleave.html')


def createleave(request):
    return render(request, 'createleave.html')


def attendance(request):
    return render(request, 'attendancelist.html')
