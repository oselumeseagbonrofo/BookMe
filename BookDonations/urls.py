from django.urls import path
from .views import HomePageView, DonatePageView

app_name = "BookDonations"
urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
]
