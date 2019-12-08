from Airbus.models import *
from django.forms import *

class loginn(Form):
    username=CharField(label='username',widget=TextInput(attrs={'placeholder':'Enter username'}))
    password = CharField(label='password', widget=PasswordInput(attrs={'placeholder': 'Enter password'}))


class signup(Form):
    username = CharField(label='username', widget=TextInput(attrs={'placeholder': 'enter username'}))
    password = CharField(label='password', widget=PasswordInput(attrs={'placeholder': 'enter password'}))
    first_name = CharField(label='firstname', widget=TextInput(attrs={'placeholder': 'enter first name'}))
    last_name = CharField(label='lastname', widget=TextInput(attrs={'placeholder': 'enter last name'}))

class coupon(Form):
    coupon_id = CharField(label='coupon_id', widget=TextInput(attrs={'placeholder': 'enter coupin id'}))
    coupon_code = CharField(label='coupon_code', widget=TextInput(attrs={'placeholder': 'enter coupin code'}))
    coupon_description = CharField(label='coupon_desciption',widget=TextInput(attrs={'placeholder': 'description'}))

class addflight(ModelForm):
    class Meta:
        model =Flight
        exclude=[]
        widgets={
            'id' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Id'}),
            'flight_id' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Flight_id'}),
            'flight_name' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Flight Name'}),
            'source' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Source'}),
            'destination' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Destination'}),
            'airlines' : TextInput(attrs={'class':'input is-info','placeholder':'Enter Airlines'}),
            'total_seats_economy': NumberInput(attrs={'placeholder': 'Enter total_seats_economy'}),
            'vacant_seats_economy': NumberInput(attrs={'placeholder': 'Enter vacant_seats_economy'}),
            'total_seats_business': NumberInput(attrs={'placeholder': 'Enter total_seats_business'}),
            'vacant_seats_business': NumberInput(attrs={'placeholder': 'Enter vacant_seats_business'}),
            'price_economy': NumberInput(attrs={'placeholder': 'Enter price_economy'}),
            'price_business': NumberInput(attrs={'placeholder': 'Enter price_business'}),
            'date': DateInput(attrs={'placeholder': 'Enter price_business'})
        }

class searchFlights(Form):
    src = CharField(label='src', widget=TextInput(attrs={'placeholder':'source'}))
    dst = CharField(label='dst', widget=TextInput(attrs={'placeholder':'destination'}))
    date = DateField(label='date', widget=DateInput())