from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from api.models import Invoice
from api.serializers import InvoiceSerializer
from rest_framework.decorators import api_view

# Create your views here.
def pdf_list(request):
    return render(request, 'pdf_list.html')

# Create your views here.
def administrator(request):
    return render(request, 'administrator.html')