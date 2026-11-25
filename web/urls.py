from django.urls import path
from . import views

urlpatterns = [
       path('', views.inicio, name='inicio'),
       path('login/', views.login, name='login'),
       path('panel/', views.panel, name='panel'),
       path('acerca/', views.panel, name='acerca')   ]