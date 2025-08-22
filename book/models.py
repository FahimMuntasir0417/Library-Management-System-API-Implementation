from django.db import models
from django.conf import settings

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    
    AVAILABLE = 'AVAILABLE'
    BORROWED = 'BORROWED'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (BORROWED, 'Borrowed'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    availability_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    published_date = models.DateField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    total_copies = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    price = models.DecimalField(max_digits=8, decimal_places=2, default=400.00) 
    
    

    def __str__(self):
        return self.title  
    
class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user} → {self.book} ({self.rating})"