from rest_framework import serializers
from .models import BorrowedRecord, BorrowedItem, BorrowedCartItem


# 2️⃣ BorrowedItem Serializer
class BorrowedItemSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="book.title", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    # product = BorrowedCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = BorrowedItem
        fields = [
            "id", "user", "user_name","book", "book_title",
            "borrow_date", "due_date", "returned", "return_date", "fine_amount",
            "created_at", "updated_at"
        ]
        read_only_fields = ["borrow_date", "created_at", "updated_at", "fine_amount"]



# 3️⃣ BorrowedCartItem Serializer
class BorrowedCartItemSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="cart_item.book.title", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    product = BorrowedItemSerializer(many=True, read_only=True)

    class Meta:
        model = BorrowedCartItem
        fields = [
            "id", "user", "user_name", "cart_item", "book_title",
            "borrow_date", "due_date", "returned", "return_date", "fine_amount" ,"product",
            # "created_at", "updated_at"
        ]
        read_only_fields = ["borrow_date", "created_at", "updated_at", "fine_amount"]







class BorrowedRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="book.title", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    cart = BorrowedCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = BorrowedRecord
        fields = [
            "id", "book", "book_title", "user", "user_name",
            "borrow_date", "due_date", "return_date", 
            "fine_amount", "status",
            "created_at", "updated_at", "cart"
        ]
        read_only_fields = ["borrow_date", "created_at", "updated_at", "fine_amount", "status"]