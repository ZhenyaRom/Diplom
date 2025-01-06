from django.contrib import admin
from .models import *


# Класс для администрирования базы данных покупателей
@ admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'date_create_buyer',)  # Выбираем поля для отображения
    list_filter = ('login', 'email', 'date_create_buyer',)  # Выбираем поля для фильтра
    search_fields = ('login', 'email', 'date_create_buyer',)  # выбираем поля для поиска


# Для базы данных видов
@ admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('name_kind',)
    search_fields = ('name_kind',)


# Для базы данных товаров
@ admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'kind', 'product_image')
    search_fields = ('name_product', 'price', 'kind', 'product_image')
    list_filter = ('name_product', 'price', 'kind', 'product_image')


# Для базы данных заказов
@ admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_order', 'date_create_order', 'active_order', 'text_order',)
    search_fields = ('id', 'author_order', 'date_create_order',)
    list_filter = ('active_order', 'date_create_order',)


# Для базы данных сообщений
@ admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')


@ admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'product', 'quantity', 'amount_product', 'order',)
    search_fields = ('id', 'buyer', 'product', 'quantity', 'amount_product', 'order',)
    list_filter = ('buyer', 'product', 'order',)
