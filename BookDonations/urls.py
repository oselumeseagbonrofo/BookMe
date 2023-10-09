from django.urls import path
from .views import HomePageView, DonatePageView, SuccessPageView, ReceivePageView, ContactPageView

app_name = "BookDonations"
urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("donate/",DonatePageView.as_view(),name="donate"),
    path("receive/",ReceivePageView.as_view(),name="receive"),
    path("success/", SuccessPageView.as_view(), name="success"),
    path("contact/",ContactPageView.as_view(), name="contact"),
]
