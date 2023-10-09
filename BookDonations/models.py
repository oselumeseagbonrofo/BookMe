from django.db import models
from django.utils import timezone
# Create your models here.
class Book_Donor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    book_amount = models.IntegerField()
    SCHOOL_CLASS_LEVEL_CHOICES = [
        ("KG", "Kindagarten"),
        ("NUR", "Nursery"),
        ("PRY", "Primary"),
        ("JSS", "Junior Secondary School"),
        ("SSS", "Senior Secondary School"),
        ("UNI", "University"),
    ]
    school_class_level = models.CharField(
        max_length=3,
        choices=SCHOOL_CLASS_LEVEL_CHOICES,
        default = "KG",
        db_index=True
    )
    drop_date = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name
  
class Book_Receiver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    book_amount = models.IntegerField()
    SCHOOL_CLASS_LEVEL_CHOICES = [
        ("KG", "Kindagarten"),
        ("NUR", "Nursery"),
        ("PRY", "Primary"),
        ("JSS", "Junior Secondary School"),
        ("SSS", "Senior Secondary School"),
        ("UNI", "University"),
    ]
    school_class_level = models.CharField(
        max_length=3,
        choices=SCHOOL_CLASS_LEVEL_CHOICES,
        default = "KG",
        db_index=True
    )
    school_name = models.CharField(max_length=100,default="OGS")
    school_location = models.CharField(max_length=100,default="Ikeja")
    drop_date = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name