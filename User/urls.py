from django.urls import path    
from . import views

urlpatterns =[
    path('Signup/', views.SignUpView),
    path('option/' ,views.Login)
]