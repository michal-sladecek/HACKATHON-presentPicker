from django.contrib import admin
from .models import ShopItem

@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    pass
