from django.urls.conf import path


from . import views

urlpatterns = [
    # path('registration/', views.registration, name="registration"),
    path('logins/', views.logins, name="logins"),
    path('employee/', views.employee),
    path('addstaff/', views.addstaff),
    path('editemployee/', views.editemployee),

    path('manageleave/', views.manageleave),
    path('createleave/', views.createleave),
    path('attendance/', views.attendance),
    path('resignation/', views.resignation),
    path('meetings/', views.meetings),
    path('notifications/', views.notifications),
    path('promotion/', views.promotion),
    path('complaints/', views.complaints),
    path('holidays/', views.holidays),
    path('dashboards/', views.dashboards),
    path('addcomplaints/', views.addcomplaints),
    path('createresignation/', views.createresignation),
    path('createpromotion/', views.createpromotion),
    path('addmeetings/', views.addmeetings),
    path('createleave/', views.createleave),
    path('designation/', views.designations, name="designation"),
    path('department/', views.departments, name="department"),
    path('leavetype/', views.leave, name="leavetype"),
    path('sample/', views.sample),

    path('employees/', views.fnemployee),
    path('editemployees/', views.fneditemployee),
    path('getdata/', views.getdata)



]
