from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from payment.forms import TransferForm
from payment.models import Customer, Balance
from payment.permissions import IsOwnerOrReadOnly
from payment.serialaizers import CustomerSerializer, UserSerializer
from django.db import transaction


def base_view(request):
    return render(request, 'base.html')


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TransferViewSet(viewsets.ViewSet):
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request):
        serializer = TransferForm(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipient_phone_number = serializer.validated_data.get('phone_number')
        amount = serializer.validated_data.get('amount')
        current_customer = request.user.customer

        try:
            recipient_customer = Customer.objects.get(phone_number=recipient_phone_number)
        except Customer.DoesNotExist:
            return Response({'error': 'Recipient not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the recipient is the same as the current customer
        if recipient_customer == current_customer:
            return Response({'error': 'Cannot transfer money to yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        # Make sure the current customer has enough balance to make the transfer
        if current_customer.balance.amount < amount:
            return Response({'error': 'Insufficient balance.'}, status=status.HTTP_400_BAD_REQUEST)

        # Perform the money transfer using database transactions
        with transaction.atomic():
            # Update the balance of the current customer
            current_customer.balance.amount -= amount
            current_customer.balance.save()

            # Update the balance of the recipient customer
            recipient_customer.balance.amount += amount
            recipient_customer.balance.save()

        return Response({'success': 'Money transferred successful.'}, status=status.HTTP_200_OK)
