from rest_framework import serializers
from .models import Cart, CartItem
from book.models import Book

class CartItemSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="book.title", read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "book", "book_title", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_items", "created_at"]
        read_only_fields = ["user", "items", "total_items"]
