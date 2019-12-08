from django.contrib import messages
from django.views import View
from Airbus.models import *
from django.shortcuts import *
from Airbus.forms.airforms import *
from django.urls import resolve
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

admin_name='admin'

def homepage(request):
    return render(request, template_name='homepage.html', context={'title': 'Airbus'})


class login_user(View):
    def get(self, request):
        # noinspection PyRedundantParentheses
        if (request.user.is_authenticated):
            return redirect('searchflight_html')
        login_form = loginn()
        return render(request, template_name='login.html', context={'form': login_form, 'title': 'Login User'})

    def post(self, request):
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('searchflight_html')
        else:
            messages.error(request, 'Invalid-credentials')
            return redirect('login_html')


class signup_user(View):
    def get(self, request):
        signup_form = signup()
        return render(request, template_name='signup.html', context={'form': signup_form, 'title': 'SignUp User'})

    def post(self, request):
        form = signup(request.POST)
        if (form.is_valid()):
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('login_html')


def logout_user(request):
    logout(request)
    return redirect('login_html')


class AddFlightView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        obj = addflight()
        return render(request, template_name='addflight.html', context={'form': obj, 'title': 'Add Flight'})

    def post(self, request):
        form = addflight(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("homepage_html")


class SearchFlightview(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        obj = searchFlights()
        if(request.user.username == admin_name):
            flag=True
        else:
            flag=False
        return render(request, template_name='searchflight.html', context={'form': obj, 'title': 'Search Flight', 'admin': flag})

    def post(self, request):
        if (request.user.username == admin_name):
            flag = True
        else:
            flag = False
        form = searchFlights(request.POST)
        if (form.is_valid()):
            src = form.cleaned_data['src']
            dst = form.cleaned_data['dst']
            date = form.cleaned_data['date']
            flights_connected1 = list(Flight.objects.raw(
                f"select * from airbus_flight f1, airbus_flight f2 where f1.source = '{src}' and f2.destination = '{dst}' and f1.destination = f2.source"))
            flights_connected2 = list(Flight.objects.raw(
                f"select * from airbus_flight f2, airbus_flight f1 where f1.source = '{src}' and f2.destination = '{dst}' and f1.destination = f2.source"))
            fligths_direct = Flight.objects.raw(f"select * from airbus_flight where source= '{src}' and destination= '{dst}'")
            flights = []
            for f in range(len(flights_connected1)):
                flight = {'connected': True}
                flight['flight1'] = flights_connected1[f]
                flight['flight2'] = flights_connected2[f]
                flights.append(flight)
            for f in fligths_direct:
                flight = {'connected': False}
                flight['flight'] = f
                flights.append(flight)

        return render(request, 'flights.html', context={'flights':flights,'admin': flag})


class book(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        flight_id = kwargs['flight_id']
        f = Flight.objects.raw(f"select * from airbus_flight where flight_id = '{flight_id}' ")
        if len(f)==0:
            return render(request, "book.html", {'error':'no flights with that id'})
        curr = f[0]
        if curr.vacant_seats_economy == 0:
            return render(request, "book.html", {'error' : 'no seats available'})
        print(curr.price_economy, curr.flight_id)
        booking = Bookings(flight_id=curr.flight_id, user_id=user.username, flight_name=curr.flight_name, source=curr.source, destination=curr.destination, airlines=curr.airlines, price_economy=curr.price_economy)
        booking.save()
        curr.vacant_seats_economy -= 1
        curr.save()
        return render(request,  template_name="book.html" , context={'error' : None, 'details' : booking })

class TransacntionView(View):
    def get(self, request):
        user = request.user
        cursor = Bookings.objects.raw(f"select * from airbus_bookings where user_id = '{user.username}'")
        bookings = []
        for i in cursor:
            bookings.append(i)
        return render(request,  template_name="transactions.html" , context={'error' : None, 'flights' : bookings})


class couponView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        obj = coupon()
        return render(request, template_name='coupon.html', context={'form': obj})

    def post(self, request):
        form = addflight(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("homepage_html")


class bookConnecting(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        flight_id = kwargs['flight_id']
        flight_id2 = kwargs['flight_id2']
        f1 = Flight.objects.raw(f"select * from airbus_flight where flight_id = '{flight_id}' ")
        f2 = Flight.objects.raw(f"select * from airbus_flight where flight_id = '{flight_id2}'")
        if len(f1) == 0 or len(f1) == 0:
            return render(request, "book.html", {'error': 'no flights with that id'})
        first = f1[0]
        second = f2[0]
        if first.vacant_seats_economy == 0 or second.vacant_seats_economy == 0:
            return render(request, "book.html", {'error': 'no seats available'})
        booking1 = Bookings(flight_id=first.flight_id, user_id=user.username, flight_name=first.flight_name,
                           source=first.source, destination=first.destination, airlines=first.airlines,
                           price_economy=first.price_economy)
        booking2 = Bookings(flight_id=second.flight_id, user_id=user.username, flight_name=second.flight_name,
                           source=second.source, destination=second.destination, airlines=second.airlines,
                           price_economy=second.price_economy)

        booking1.save()
        booking2.save()
        first.vacant_seats_economy -= 1
        second.vacant_seats_economy -= 1
        booking = {'source':first.source, 'destination':first.destination, 'price_economy':first.price_economy, 'flight_name':first.flight_name,'user_id':user.username}
        first.save()
        second.save()
        return render(request, template_name="book.html", context={'error': None, 'details': booking})


class offersView(View):
    def get(self, request):
        cursor = Coupon.objects.raw(f"select * from airbus_coupon")
        bookings = []
        for i in cursor:
            bookings.append(i)
        return render(request,  template_name="offers.html" , context={'error' : None, 'coupons' : bookings})
