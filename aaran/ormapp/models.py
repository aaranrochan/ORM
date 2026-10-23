from django.db import models
from django.contrib import admin


class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_delivered = models.BooleanField()


class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'food_item', 'quantity', 'price', 'is_delivered')