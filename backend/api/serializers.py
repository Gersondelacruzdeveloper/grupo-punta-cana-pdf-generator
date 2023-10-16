from rest_framework import serializers
from .models import Template, GeneratedBoardingPass, Invoice, Advertisement, Template

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class GeneratedBoardingPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedBoardingPass
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class AdminTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['name', 'content', 'type', 'active']