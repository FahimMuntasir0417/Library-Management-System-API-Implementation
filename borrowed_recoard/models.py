from django.db import models
from django.conf import settings
from book.models import Book
from order.models import Cart, CartItem

User = settings.AUTH_USER_MODEL


# 1️⃣ BorrowedRecord → direct user–book relation
class BorrowedRecord(models.Model):
    STATUS_CHOICES = (
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"


# 2️⃣ BorrowedItem → specific borrowed item (independent of Cart)
class BorrowedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed_items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowed_items")
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    return_date = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username}"


# 3️⃣ BorrowedCartItem → borrow operation based on a Cart
class BorrowedCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed_cart_items")
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE, related_name="borrowed_cart_items")
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    return_date = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart_item.book.title} borrowed by {self.user.username}"
