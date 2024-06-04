from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookingVizardView.as_view())
]