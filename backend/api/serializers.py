# serializers.py
from rest_framework import serializers
from .models import (CustomUser,
                     Template,
                     GeneratedBoardingPass,
                     Invoice,
                     Advertisement)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id', 'name', 'content', 'type', 'active')


class GeneratedBoardingPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedBoardingPass
        fields = ('id', 'user', 'template', 'pdf_data', 'generated_at',
                  'passenger_name', 'seat_number', 'departure_date', 'boarding_gate')


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('id', 'user', 'template', 'invoice_number', 'issue_date', 'due_date',
                  'customer', 'products_or_services', 'subtotal', 'tax', 'total_amount')


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('id', 'user', 'template', 'price', 'date_created',
                  'date_posted', 'place', 'location')
