from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.apiOverview),
    path('pdf_list',views.pdf_list),
    path('admin_list',views.admin_list),
    path('add_template',views.add_template)
]
