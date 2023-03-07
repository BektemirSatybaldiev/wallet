from django.contrib.auth import get_user_model
from rest_framework import serializers
from payment.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['balance'] = instance.balance.amount
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
