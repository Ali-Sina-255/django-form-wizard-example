from django import forms
from . models import Guest, Business, Booking
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