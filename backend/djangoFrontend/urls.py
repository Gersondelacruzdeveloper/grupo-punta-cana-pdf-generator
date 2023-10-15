from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pdf_list, name="pdf_list"),
    path('administrator/', views.administrator, name="administrator"),
]
