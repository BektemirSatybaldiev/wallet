from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=False, unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    date_of_birth = models.DateField(max_length=150, blank=False)
    verified = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^996\d{9}$',
                                 message="Phone number must be entered in the format: '996*********'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True, unique=True)

    def __str__(self):
        return self.username


class Balance(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return f"Customer {self.customer} has {self.amount}$"
