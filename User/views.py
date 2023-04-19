from django.shortcuts import render , HttpResponse
from django.core.exceptions import BadRequest
from django.http import StreamingHttpResponse
from . import forms
from rest_framework.parsers import JSONParser
from django.contrib.auth import models , authenticate
from serializers import MessageSerializer
# Create your views here.

def SignUpView(request):
    if request.method == "POST":
        f = forms.UserSignup(request.POST )
        if f.is_valid():
            f.save()
        else :
            raise BadRequest("fill form data correctly")
    elif request.method == "GET":
        form = forms.UserSignup()
        return render(request , 'signup.html' ,{'form':form})
    

def checkMessage(request):
    data = JSONParser().parser(request)
    serializer = MessageSerializer(data = data)
    if serializer.data['signInMethod'] == 'EmailSignin' :
        pass
    pass

def Login(request):
    emailSignIn = forms.UserSigninEmail()
    usernameSignIn = forms.UserSigninUsername()
    if request.method == 'GET':
        return render(request,"option.html",{'emailform':emailSignIn,'usernameform':usernameSignIn})
    elif request.method == 'POST':
        f = forms.UserSigninEmail(request.POST)
        if f.is_valid() :
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            user = authenticate(email=email , password = password)
            if user is not None:
                #user authentication is successfull
                #It redirects to a page personalized for the user
                pass
            else:
                #user authentication is not successful
                #Give some message to the user regarding the wrong password
                
                pass
            

