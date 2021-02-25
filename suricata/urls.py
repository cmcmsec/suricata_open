from django.urls import path
from . import views


urlpatterns = [
    path('', views.rule),
    path('index/', views.rule),
    path('rule/', views.rule),
    path('monitor/', views.monitor),
    path('savesuri/', views.savesuri),
    path('morlist/', views.morlist),
    path('edit_mornitor/<int:suid>/', views.edit_mornitor),
    path('delmor/<int:suid>/', views.delmor)



]
