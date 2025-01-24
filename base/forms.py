from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Customer
        fields = ('username','name', 'email', 'password1', 'password2')  

class OwnerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Owner
        fields = ('username','name', 'email', 'password1', 'password2')  

class DelivererSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Deliverer
        fields = ('username','name', 'email', 'password1', 'password2')  

class RestaurantCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True


    class Meta:
        model = Restaurant
        fields = ('name1','image','description')
        required = ['name1','image']

class ItemForm(ModelForm):
    class Meta:
        model = Items
        # fields = ['name','price','description','category',
        #           'image','quantity', 'offer','cusine'
        #           ]
        exclude = ['rating','restaurant']
