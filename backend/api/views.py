from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Invoice,GeneratedBoardingPass,Advertisement,Template
from .serializers import (InvoiceSerializer, GeneratedBoardingPassSerializer,
                          AdvertisementSerializer, TemplateSerializer, AdminTemplateSerializer
                          )
from .utils import get_template_content
from django.views.decorators.csrf import csrf_protect
# from .models import CustomUser

# Create your views here.
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def apiOverview(request):
	api_urls = {
		'List':'api/pdf_list/',
		'Admin List':'admin_list/',
		'Create Template':'api/add_template/',
		'Update':'api/template-update/<str:pk>/',
		'Delete':'api/template-delete/<str:pk>/',
        'Register User':'api/register_user',
        'Login User':'api/login_user',
		}
	return Response(api_urls)


# all the models query here together
@api_view(['GET'])
def pdf_list(request):
	# invoice
	invoices = Invoice.objects.all()
	invoices_serializer = InvoiceSerializer(invoices, many=True)
	# advertisement
	advertisement = Advertisement.objects.all()
	advertisement_serializer = AdvertisementSerializer(advertisement, many=True)
	# GeneratedBoardingPass
	boardingPass = GeneratedBoardingPass.objects.all()
	boarding_pass_serializer = GeneratedBoardingPassSerializer(boardingPass, many=True)
	# filter advertisement template
	template_ads= Template.objects.filter(type="Advertisement", active=True)
	template_boardings= Template.objects.filter(type="BoardingPass", active=True)
	template_invoiceses= Template.objects.filter(type="Invoice", active=True)
    # get the template contents
	template_ads_content = get_template_content(template_ads)
	template_boarding_content = get_template_content(template_boardings)
	template_invoice_content = get_template_content(template_invoiceses)
	combined_data = {
		"invoices": (invoices_serializer.data, template_invoice_content),
		"advertisement":(advertisement_serializer.data, template_ads_content),
		"boarding_pass": (boarding_pass_serializer.data, template_boarding_content),
	}
	return Response(combined_data)


# all the models query here together
@api_view(['GET'])
def admin_list(request):
	# filter advertisement template
	template_ads= Template.objects.filter(type="Advertisement")
	template_boardings= Template.objects.filter(type="BoardingPass")
	template_invoiceses= Template.objects.filter(type="Invoice")
	# serialize the data
	template_ads_serializer = TemplateSerializer(template_ads, many=True)
	template_boardings_serializer= TemplateSerializer(template_boardings, many=True)
	template_invoiceses_serializer = TemplateSerializer(template_invoiceses, many=True)
    # combine data
	combined_data = {
		"template_ads": template_ads_serializer.data,
		"template_boardings":template_boardings_serializer.data,
		"template_invoiceses": template_invoiceses_serializer.data,
	}
	return Response(combined_data)

# all the models query here together
# all the models query here together
@api_view(['POST'])
def add_template(request):
    if request.method == "POST":
        data = request.data
        serializer = AdminTemplateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Template created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)