from django.urls import path
from .views import HomePageView, DonatePageView, SuccessPageView

app_name = "BookDonations"
urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("donate/",DonatePageView.as_view(),name="donate"),
    path("success/", SuccessPageView.as_view(), name="success")
]
