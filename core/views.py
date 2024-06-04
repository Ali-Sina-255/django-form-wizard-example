from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .form import GestDetailForm, BusinessDetailForm, BookingDetailForm

def show_business_from(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return cleaned_data.get('is_business_guest')

class BookingVizardView(SessionWizardView):
    form_list = [GestDetailForm, BusinessDetailForm,BookingDetailForm]
    template_name = 'core/index.html'
    condition_dict = {'1':show_business_from}
 
    def done(self, form_list, **kwargs):
        guest_form = form_list[0]
        if guest_form.cleaned_data.get('is_business_guest'):
            business = form_list[1].save()
            guest = guest_form.save(commit=False)
            guest.business = business
            guest.save()
        else:
            guest = guest_form.save()
        booking = form_list[-1].save(commit=False)
        booking.guest = guest
        booking.save()
        return HttpResponse('form is submitted')
    
