from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class HomePageView(TemplateView):
    template_name = "BookDonations/index.html"
    
class DonatePageView(FormView):
    template_name= "BookDonations/donate.html"

