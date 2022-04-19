from django.contrib import admin

from .models import Data

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "rent", "emi", "tax", "exp")
    list_filter = ("name", "rent")

