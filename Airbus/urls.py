from django.urls import path

from Airbus.views import *

urlpatterns = [
    path('',homepage,name='homepage_html'),
    path('login/',loginuser.as_view(), name='login_html'),
    path('signup/',Signupuser.as_view(),name='signup_html'),
    path('logout/',logout_user,name='logout_html')
]