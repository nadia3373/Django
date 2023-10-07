from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ("name", "email", "phone_number")
    list_filter = ("registration_date",)
    search_fields = ("name", "email", "phone_number")
    search_help_text = "Поиск по имени, email, номеру телефона"
    ordering = ("name",)
    fieldsets = (
        (None, {
            "fields": ("name",)
        }),
        ("Контактная информация", {
            "fields": ("email", "phone_number", "address")
        }),
        ("Служебная информация", {
            "description": "Дата регистрации устанавливается автоматически при регистрации покупателя",
            "fields": ("registration_date",)
        }),
    )
    readonly_fields = ("registration_date",)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("name", "price", "quantity")
    list_filter = ("added_date",)
    search_fields = ("name", "description")
    search_help_text = "Поиск по названию, описанию"
    ordering = ("name",)
    fieldsets = (
        (None, {
            "fields": ("name", "description", "price", "quantity", "photo")
        }),
        ("Служебная информация", {
            "description": "Дата добавления устанавливается автоматически при создании товара",
            "fields": ("added_date",)
        }),
    )
    readonly_fields = ("added_date",)


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ("id", "client", "order_date", "total_amount")
    list_filter = ("order_date",)
    search_fields = ("client__name", "products__name")
    search_help_text = "Поиск по имени покупателя, названию товара"
    ordering = ("-id",)
    fieldsets = (
        (None, {
            "fields": ("client", "products", "total_amount")
        }),
        ("Служебная информация", {
            "description": "Дата создания устанавливается автоматически при оформлении заказа",
            "fields": ("order_date",)
        }),
    )
    readonly_fields = ("order_date",)
