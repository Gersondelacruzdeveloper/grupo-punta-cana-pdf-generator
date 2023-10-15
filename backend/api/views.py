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
                          AdvertisementSerializer, TemplateSerializer
                          )
from .utils import get_template_content
# from .models import CustomUser

# Create your views here.
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def apiOverview(request):
	api_urls = {
		'List':'api/pdf_list/',
		'Detail View':'api/template-detail/<str:pk>/',
		'Create':'api/template-create/',
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













# @api_view(["POST"])
# @permission_classes([permissions.AllowAny])
# def register_user(request):
#     if request.method == "POST":
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             response_data = {
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh)
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# @permission_classes([permissions.AllowAny])
# def login_user(request):
#     if request.method == "POST":
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             response_data = {
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh)
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         return Response({"message": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)