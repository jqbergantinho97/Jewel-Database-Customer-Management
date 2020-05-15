# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'jewels/dashboard.html')


def products(request):
    return render(request, 'jewels/products.html')


def customer(request):
    return render(request, 'jewels/customer.html')