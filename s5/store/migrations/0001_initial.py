# Generated by Django 4.2.5 on 2023-10-07 02:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15, verbose_name='номер телефона')),
                ('address', models.TextField(verbose_name='адрес')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата регистрации')),
            ],
            options={
                'verbose_name': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='количество')),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата добавления')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product_photos/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client', verbose_name='покупатель')),
                ('products', models.ManyToManyField(to='store.product', verbose_name='товары')),
            ],
            options={
                'verbose_name': 'Заказы',
            },
        ),
    ]