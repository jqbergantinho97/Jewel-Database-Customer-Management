# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=10000, null=True)
    profile_pic = models.ImageField(default="profile1.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Pulsera', 'Pulsera'),
        ('Collar', 'Collar'),
        ('Gemelos', 'Gemelos'),
        ('Anillo', 'Anillo'),
        ('Llavero', 'Llavero'),
    )

    name = models.CharField(max_length=200, null=True)
    product_pic = models.ImageField(default="", null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    size = models.FloatField(null=True)
    material = models.CharField(max_length=10000, null=True)
    cost_price = models.FloatField(null=True)
    sell_price = models.FloatField(null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    units = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Enviado', 'Enviado'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name

