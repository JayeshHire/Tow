from django.urls import path    
from . import views

urlpatterns =[
    path('test/',views.test),
    path('Signup/', views.SignUpView),
    path('option/' ,views.Login),
    path('Signup/passVerification/',views.passInputform),
    path('Signup/passVerification/submission/',views.submission)
]