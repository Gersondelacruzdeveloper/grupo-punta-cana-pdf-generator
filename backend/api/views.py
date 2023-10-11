from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'api/template-list/',
		'Detail View':'api/template-detail/<str:pk>/',
		'Create':'api/template-create/',
		'Update':'api/template-update/<str:pk>/',
		'Delete':'api/template-delete/<str:pk>/',
		}
	return Response(api_urls)