from rest_framework import serializers
from .models import Book, BookAuthor, BookCategory ,Review

# -------------------------
# Author Serializer
# -------------------------
class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = '__all__'

# -------------------------
# Category Serializer
# -------------------------
class BookCategorySerializer(serializers.ModelSerializer):
    # যদি চাও, category এর সাথে সব books list দেখাবে
    books = serializers.StringRelatedField(many=True, read_only=True)  # related_name='books' from Book model

    class Meta:
        model = BookCategory
        fields = ['id', 'name', 'description', 'books']

# -------------------------
# Book Serializer
# -------------------------
class BookSerializer(serializers.ModelSerializer):
    # Read-only nested fields for display
    author_name = serializers.CharField(source='author.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    # Writable primary keys for updates/creates
    author = serializers.PrimaryKeyRelatedField(queryset=BookAuthor.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=BookCategory.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "book", "user", "user_name", "rating", "comment", "created_at"]
        read_only_fields = ["user", "book"]