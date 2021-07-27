from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('employee/', views.employee),
    path('addstaff/', views.addstaff),
    path('editemployee/', views.editemployee),
    path('manageleave/', views.manageleave),
    path('createleave/', views.createleave),
    path('attendance/', views.attendance),
    path('resignation/', views.resignation),
    path('meetings/', views.meetings),
    path('notifications/', views.notifications),


]
