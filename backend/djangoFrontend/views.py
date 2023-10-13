from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {"name":"<h1>gerson</h1>"}
    return render(request, 'home.html')
