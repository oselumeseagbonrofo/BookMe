from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse

from .models import Book_Donor
from .forms import BookDonorForm
class HomePageView(TemplateView):
    template_name = "BookDonations/index.html"

class DonatePageView(View):
    form_class = BookDonorForm
    initial = {"key": "value"} 
    template_name = "BookDonations/donate.html"
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(reverse("BookDonations:success")) 
           

class SuccessPageView(TemplateView):
    template_name = "BookDonations/success.html"