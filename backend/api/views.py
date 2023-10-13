from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, permissions
# from .models import CustomUser

# Create your views here.
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def apiOverview(request):
	api_urls = {
		'List':'api/template-list/',
		'Detail View':'api/template-detail/<str:pk>/',
		'Create':'api/template-create/',
		'Update':'api/template-update/<str:pk>/',
		'Delete':'api/template-delete/<str:pk>/',
        'Register User':'api/register_user',
        'Login User':'api/login_user',
		}
	return Response(api_urls)













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