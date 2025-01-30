from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author =  models.CharField(max_length=255, default="No author")
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    borrowing_price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.book.title} ({self.rating}/5)'
