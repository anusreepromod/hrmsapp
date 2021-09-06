from django.shortcuts import render

# Create your views here.


def logins(request):
    return render(request, 'logins.html')


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


def resignation(request):
    return render(request, 'resignation.html')


def meetings(request):
    return render(request, 'meetings.html')


def notifications(request):
    return render(request, 'notifications.html')


def promotion(request):
    return render(request, 'promotion.html')


def complaints(request):
    return render(request, 'complaints.html')


def holidays(request):
    return render(request, 'holidays.html')


def dashboards(request):
    return render(request, 'dashboards.html')


def addcomplaints(request):
    return render(request, 'addcomplaints.html')


def createresignation(request):
    return render(request, 'createresignation.html')


def createpromotion(request):
    return render(request, 'createpromotion.html')


def addmeetings(request):
    return render(request, 'addmeetings.html')


def createleave(request):
    return render(request, 'createleave.html')
