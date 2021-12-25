from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Machine_Design(request):
    return render(request, 'Machine_Design.html')
def Learn(request):
    return render(request, 'Learn.html')
def Services(request):
    return render(request, 'Services.html')
def AboutUs(request):
    return render(request, 'About.html')
def Cotter_Joint(request):
    return render(request, 'Cotter_Joint.html')
def Cotter_Solution(request):
    return render(request, 'Cotter_Solution.html')
def Forgot_Password(request):
    return render(request, 'Forgot_Password.html')
def Learn_Cotter_Joint(request):
    return render(request, 'Learn_Cotter_Joint.html')
def Login(request):
    return render(request, 'Login.html')
def Privacy_Policy(request):
    return render(request, 'Privacy_Policy.html')
def Signup(request):
    return render(request, 'Signup.html')
def Terms(request):
    return render(request, 'Terms.html')