from django.urls import path

from Airbus.views import *
from Airbus.news_controller import *

urlpatterns = [
    path('',SearchFlightview.as_view(),name='homepage_html'),
    path('login/', login_user.as_view(), name='login_html'),
    path('signup/', signup_user.as_view(), name='signup_html'),
    path('logout/', logout_user, name='logout_html'),
    path('addflight/', AddFlightView.as_view(), name="addflight_html"),
    path('searchflight/', SearchFlightview.as_view(), name="searchflight_html"),
    path('searchflight/book/<str:flight_id>/', book.as_view(), name="book"),
    path('searchflight/book/<str:flight_id>/<str:flight_id2>/', bookConnecting.as_view(), name="bookconnect"),
    path('news/', posts, name="posts"),
    path('test/', test_scroll, name="test"),
    path('populate/', populate_posts, name="populate"),
    path('transactions/',TransacntionView.as_view(),name='transactions_html'),
    path('addcoupons/',couponView.as_view(),name='coupon_html'),
    path('offers/',offersView.as_view(),name='offers_html')
]