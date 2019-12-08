from django.urls import path

from Airbus.views import *
from Airbus.news_controller import *

urlpatterns = [
    path('',homepage,name='homepage_html'),
    path('login/', login_user.as_view(), name='login_html'),
    path('signup/', signup_user.as_view(), name='signup_html'),
    path('logout/', logout_user, name='logout_html'),
    # path('news/', posts, name="posts"),
    # path('test/', test_scroll, name="test"),
    # path('populate/', populate_posts, name="populate")
]