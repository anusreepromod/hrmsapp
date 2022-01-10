from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('login/', views.fnlogin),
    path('master/', views.master),
    path('dashboard/', views.dashboard),
    path('editprofile/', views.editprofile),
    path('leave/', views.leaves),
    path('applyleave/', views.applyleave, name="applyleave"),
    path('notification/', views.notifications),
    path('leavedetail/', views.leavedetail),
    path('fnleave/', views.fnleave, name='fnleave'),
    path('userprofile/', views.userprofile),
    path('getuserprofile/', views.getuserprofile, name='getuserprofile'),
    path('settings/', views.settings),
    path('attendance/', views.attendance),
    path('fnattendance/', views.fnattendance),
    path('holiday/', views.holidays),
    path('getcheckin/', views.fncheckin),
    path('getcheckout/', views.fncheckout),
    path('logout/', views.fnlogout, name='logout'),
    path('getmeeting/', views.getmeeting, name='getmeeting'),
    path('getdatas/', views.getdatas, name='getdatas'),
    path('resignations/', views.resignations, name='resignations'),
    path('addresignation/', views.addresignation, name='addresignation'),
    path('fnresignations/', views.fnresignations),
    path('getresignation/', views.getresignation),
    path('updateresignation/', views.updateresignation, name="updateresignation"),

]
