from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name='signup'), 
    path('signin/', views.signin, name='signin'),  
    path('logout/', views.logout_view, name='logout'),  
]
