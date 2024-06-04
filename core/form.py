from typing import Any
from django import forms
from . models import Guest, Business, Booking, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','phone_number']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class GestDetailForm(forms.ModelForm):
    RADIO_SELECT = [(True,'Yes',),(False,'No')]

    is_business_guest = forms.BooleanField(widget=forms.RadioSelect(choices=RADIO_SELECT), required=False)
    class Meta:
        model = Guest
        fields = ["first_name","last_name","email",'phone']


class BusinessDetailForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name']

class BookingDetailForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room_type','date','number_of_nights']
        widget = {"data":forms.DateInput(attrs={'type':'date'})}