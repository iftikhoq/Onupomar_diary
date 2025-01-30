from django.db import models
from django.contrib.auth.models import User
from .constants import  GENDER_TYPE
from book.models import Book

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    join_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) 
    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowers")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} borrowed_at {self.borrowed_at}"

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Deposited")
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2) 
    dep_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.user.first_name} deposited {self.amount}"