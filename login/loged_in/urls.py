from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('loginprocess/',views.loginprocess,name='loginprocess'),
    path('signup/',views.signup,name='signup'),
    path('signup/signupprocess/',views.signupprocess,name='signupprocess'),
]