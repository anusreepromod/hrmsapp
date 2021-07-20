from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('editprofile/', views.editprofile),
    path('leave/', views.leave),
    path('applyleave/', views.applyleave),
    path('notification/', views.notification),
    path('leavedetail/', views.leavedetail),
    path('userprofile/', views.userprofile),
    path('settings/', views.settings),
    path('attendance/', views.attendance),

]
