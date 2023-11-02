from django.contrib import admin
from .models import Vech
# Register your models here.
@admin.register(Vech)
class VechAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']