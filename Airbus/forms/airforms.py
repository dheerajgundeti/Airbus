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

