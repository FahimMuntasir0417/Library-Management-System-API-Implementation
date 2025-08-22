from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta

from .models import BorrowedRecord, BorrowedItem, BorrowedCartItem
from .serializers import BorrowedRecordSerializer, BorrowedItemSerializer, BorrowedCartItemSerializer


# Fine calculation helper
def calculate_fine(due_date, return_date, rate=10):
    if return_date > due_date:
        days_overdue = (return_date - due_date).days
        return days_overdue * rate
    return 0


# 1️⃣ BorrowedRecordViewSet
class BorrowedRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowedRecord.objects.all()
    serializer_class = BorrowedRecordSerializer

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        record = self.get_object()
        record.return_date = now()
        record.status = "returned"
        record.fine_amount = calculate_fine(record.due_date, record.return_date)
        record.save()
        return Response(BorrowedRecordSerializer(record).data)


# 2️⃣ BorrowedItemViewSet
class BorrowedItemViewSet(viewsets.ModelViewSet):
    queryset = BorrowedItem.objects.all()
    serializer_class = BorrowedItemSerializer

    @action(detail=True, methods=["post"])
    def return_item(self, request, pk=None):
        item = self.get_object()
        item.return_date = now()
        item.returned = True
        item.fine_amount = calculate_fine(item.due_date, item.return_date)
        item.save()
        return Response(BorrowedItemSerializer(item).data)


# 3️⃣ BorrowedCartItemViewSet
class BorrowedCartItemViewSet(viewsets.ModelViewSet):
    queryset = BorrowedCartItem.objects.all()
    serializer_class = BorrowedCartItemSerializer

    @action(detail=True, methods=["post"])
    def return_cart_item(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.return_date = now()
        cart_item.returned = True
        cart_item.fine_amount = calculate_fine(cart_item.due_date, cart_item.return_date)
        cart_item.save()
        return Response(BorrowedCartItemSerializer(cart_item).data)
