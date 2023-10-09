from django.forms import ModelForm
from .models import Book_Donor, Book_Receiver
from django.utils.translation import gettext_lazy as _

# form for book donor page
class BookDonorForm(ModelForm):    
    class Meta:
        model = Book_Donor
        fields = "__all__"

# form for Book receiver page       
class BookReceiverForm(ModelForm):
    class Meta:
        model = Book_Receiver
        fields = ["first_name","last_name","book_amount","school_class_level","school_name","school_location","drop_date","phone_number","email"]
        # changes default label of some model data
        labels = {
            "book_amount": _("Number of books"),
            "drop_date": _("Pick up date"),
        }
        