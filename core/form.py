from django import forms
from . models import Guest
class GestDetailForm(forms.ModelForm):
    RADIO_SELECT = [(True,'Yes',),(False,'No')]

    is_business_guest = forms.BooleanField(widget=forms.RadioSelect(choices=RADIO_SELECT), required=False)
    class Meta:
        model = Guest
        fields = ["first_name","last_name","email",'phone']