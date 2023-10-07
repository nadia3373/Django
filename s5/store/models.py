from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, verbose_name="номер телефона")
    address = models.TextField(verbose_name="адрес")
    registration_date = models.DateTimeField(default=timezone.now, verbose_name="дата регистрации")

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    quantity = models.PositiveIntegerField(verbose_name="количество")
    added_date = models.DateTimeField(default=timezone.now, verbose_name="дата добавления")
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True, verbose_name="изображение")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="покупатель")
    products = models.ManyToManyField(Product, verbose_name="товары")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма")
    order_date = models.DateTimeField(default=timezone.now, verbose_name="дата заказа")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.id} клиента {self.client.name}"
