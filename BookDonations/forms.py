from django.forms import ModelForm
from .models import Book_Donor

class BookDonorForm(ModelForm):    
    class Meta:
        model = Book_Donor
        fields = "__all__"
