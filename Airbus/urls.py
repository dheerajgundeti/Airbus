from django.urls import path

from Airbus.views import *

urlpatterns = [
    path('',homepage,name='homepage_html'),
    path('login/', login_user.as_view(), name='login_html'),
    path('signup/', signup_user.as_view(), name='signup_html'),
    path('logout/', logout_user, name='logout_html')
]