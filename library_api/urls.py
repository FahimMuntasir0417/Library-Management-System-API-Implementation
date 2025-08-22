from django.urls import path, include
from rest_framework_nested import routers
from book.views import (
    BookViewSet, BookCategoryViewSet, BookAuthorViewSet, ReviewViewSet
)
from order.views import CartViewSet, CartItemViewSet

from borrowed_recoard.views import (
    BorrowedRecordViewSet, BorrowedItemViewSet, BorrowedCartItemViewSet

)
# Main router
router = routers.DefaultRouter()
router.register('categories', BookCategoryViewSet, basename='categories')
router.register('authors', BookAuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')
router.register(r'carts', CartViewSet, basename='carts')
router.register(r'borrowed-records', BorrowedRecordViewSet, basename='borrowed-records')

# Nested router for reviews under books
books_router = routers.NestedDefaultRouter(router, r'books', lookup='book')
books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')

cart_router = routers.NestedDefaultRouter(router, r'carts', lookup='cart')
cart_router.register(r'items', CartItemViewSet, basename="cart-items")

borrow_cart_router = routers.NestedDefaultRouter(router, r'borrowed-records', lookup='borrowedrecord')
borrow_cart_router.register(r'cart-items', BorrowedCartItemViewSet, basename='borrowed-cart-items')

# Nested router: BorrowedItem under BorrowedCartItem
borrow_item_router = routers.NestedDefaultRouter(borrow_cart_router, r'cart-items', lookup='cartitem')
borrow_item_router.register(r'items', BorrowedItemViewSet, basename='borrowed-cart-item-items')





urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('', include(cart_router.urls)),# 👈 nested urls
    path('', include(borrow_cart_router.urls)),     # 👈 borrowed-record -> items
    path('', include(borrow_item_router.urls)) # 👈 borrowed-item -> cart-items
]
