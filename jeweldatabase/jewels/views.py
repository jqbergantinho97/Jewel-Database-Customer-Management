# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter, CustomerFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@unauthenticated_user
def registerPage(request):
        form = CreateUserForm

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                #group = Group.objects.get(name='customer')
                #user.groups.add(group)
                #Customer.objects.create(
                #    user = user,
                 #   name = user.username
                #)

                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {"form": form}
        return render(request, 'jewels/register.html', context)


@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'jewels/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'delivered': delivered,
               'pending': pending,
               'total_orders': total_orders
               }
    return render(request, 'jewels/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    user = request.user.customer
    form = CustomerForm(instance=user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save

    context = {'form': form}
    return render(request, 'jewels/account_settings.html', context)


@login_required(login_url='login')
@admin_only
def home(request):
    all_orders = Order.objects.all()
    orders = Order.objects.all().order_by('-id')[:5]

    customers = Customer.objects.all()

    total_customers = customers.count()
    customers = Customer.objects.all().order_by('-date_created')[:5]
    total_orders = all_orders.count()
    delivered = all_orders.filter(status='Enviado').count()
    pending = all_orders.filter(status='Pendiente').count()

    context = {
        'orders': orders,
        'customers': customers,
        'delivered': delivered,
        'pending': pending,
        'total_customers': total_customers,
        'total_orders': total_orders
    }
    return render(request, 'jewels/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product,
               }

    return render(request, 'jewels/product.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'jewels/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer,
               'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter
               }

    return render(request, 'jewels/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request):
    customers = Customer.objects.all().order_by('-date_created')

    myFilter = CustomerFilter(request.GET, queryset=Customer.objects.all())
    customers = myFilter.qs

    context = {
        'customers': customers,
        'myFilter': myFilter,
    }
    return render(request, 'jewels/customers.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    CustomerFormSet = inlineformset_factory(Customer, fields=('name', 'phone'))


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print("Printing POST: ", request.POST)
        formset= OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'jewels/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        #print("Printing POST: ", request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'formset':form}
    return render(request, 'jewels/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}

    return render(request, 'jewels/delete.html', context)