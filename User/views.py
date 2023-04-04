from django.shortcuts import render , HttpResponse
from django.views
from django.http import StreamingHttpResponse
from . import forms
# Create your views here.

def SignUpView(request):
    if request.method == "POST":
        f = forms.UserSignup(request.POST )
        if f.is_valid():
            f.save()
        else :
            
