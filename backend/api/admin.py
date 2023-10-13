# Register all models here.
from django.contrib import admin
from .models import Template, GeneratedBoardingPass, Invoice, Advertisement
admin.site.register(Template),
admin.site.register(GeneratedBoardingPass),
admin.site.register(Invoice),
admin.site.register(Advertisement),

