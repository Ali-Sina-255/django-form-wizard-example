from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from .form import GestDetailForm
# Create your views here.
class BookingVizardView(SessionWizardView):
    form_list = [GestDetailForm]
    template_name = 'core/index.html'

    def done(self, form_list, **kwargs):
        return HttpResponse('form is submitted')