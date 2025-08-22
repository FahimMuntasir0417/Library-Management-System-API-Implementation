from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book, BookAuthor, BookCategory , Review
from book.serializers import BookSerializer, BookAuthorSerializer, BookCategorySerializer , ReviewSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    

class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
# class ReviewViewSet(viewsets.ModelViewSet):
#     serializer_class = ReviewSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         book_id = self.kwargs.get("book_pk")   # nested router থেকে আসবে
#         return Review.objects.filter(book_id=book_id)

#     def perform_create(self, serializer):
#         book_id = self.kwargs.get("book_pk")
#         serializer.save(user=self.request.user, book_id=book_id)

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs.get("book_pk")
        return (
            Review.objects.filter(book_id=book_id)
            .select_related("user", "book")   # ✅ এখানে যোগ করা হলো
        )

    def perform_create(self, serializer):
        book_id = self.kwargs.get("book_pk")
        serializer.save(user=self.request.user, book_id=book_id)