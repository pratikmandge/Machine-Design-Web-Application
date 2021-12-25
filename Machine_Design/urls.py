from django.urls import path
from . import views

urlpatterns = [
    path('', views.Machine_Design, name='Machine_Design'),
    path('About_Us', views.AboutUs, name='About_Us'),
    path('Learn', views.Learn, name='Learn'),
    path('Services', views.Services, name='Services'),
    path('Cotter_Joint', views.Cotter_Joint, name='Cotter_Joint'),
    path('Cotter_Solution', views.Cotter_Solution, name='Cotter_Solution'),
    path('Forgot_Password', views.Forgot_Password, name='Forgot_Password'),
    path('Learn_Cotter_Joint', views.Learn_Cotter_Joint, name='Learn_Cotter_Joint'),
    path('Login', views.Login, name='Login'),
    path('Privacy_Policy', views.Privacy_Policy, name='Privacy_Policy'),
    path('Signup', views.Signup, name='Signup'),
    path('Terms', views.Terms, name='Terms')
]