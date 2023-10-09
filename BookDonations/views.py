from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse

from .models import Book_Donor
from .forms import BookDonorForm, BookReceiverForm
class HomePageView(TemplateView):
    template_name = "BookDonations/index.html"

class DonatePageView(View):
    form_class = BookDonorForm
    initial = {"key": "value"} 
    template_name = "BookDonations/donate.html"
    
    # Handles GET requests
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    
    # Handles POST requests
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(reverse("BookDonations:success")) 
            
class ReceivePageView(View):
    form_class = BookReceiverForm
    initial = {"key": "value"} 
    template_name = "BookDonations/receive.html"
    
    # Handles GET requests
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    
    # Handles POST requests
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(reverse("BookDonations:success")) 
       
class SuccessPageView(TemplateView):
    template_name = "BookDonations/success.html"

class ContactPageView(TemplateView):
    template_name = "BookDonations/contact.html"