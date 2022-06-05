from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from customer.models import CustomerProfile
from customer.decorator import admin_only
from .forms import UpdateOrderForm, ProductAddForm
from .models import Product, Order

@login_required(login_url='customer:login')
@admin_only
def adminHomeView(request):
   order = Order.objects.all()
   customer = CustomerProfile.objects.all()
   total_order = order.count()
   delivered = Order.objects.filter(status='Delivered').count()
   pending = Order.objects.filter(status='Pending').count()

   context = {
      'orders':order,
      'total_order':total_order,
      'customer':customer,
      'delivered':delivered,
      'pending':pending,
   }
   return render(request, 'products/dashboard.html', context)

@login_required(login_url='customer:login')
def customerHomeView(request):
   orders = request.user.customerprofile.order_set.all()
   total_order = orders.count()
   delivered_count = orders.filter(status='Delivered').count()
   pending_count = orders.filter(status='Pending').count()

   context ={
      'orders':orders,
      'total_order':total_order,
      'delivered':delivered_count,
      'pending':pending_count,
   }
   return render(request, 'products/user.html', context)

@login_required(login_url='customer:login')
@admin_only
def product_list(request):
   products = Product.objects.all()
   context = {
      'products':products,
   }
   return render(request, 'products/products.html', context)

@login_required(login_url='customer:login')
def add_product(request):
   form = ProductAddForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('products:product_list')
   context = {
      'form':form
   }
   return render(request, 'products/add_product.html', context)

@login_required(login_url='customer:login')
def createOrder(request):
   context = {

   }
   return render(request, 'products/createOrder.html', context)

@login_required(login_url='customer:login')
def updateOrder(request,pk):
   order = get_object_or_404(Order,id=pk)
   order_form = UpdateOrderForm(request.POST or None, instance=order)
   if order_form.is_valid():
      print(order_form.cleaned_data)
      order_form.save()
      return redirect('customer:customer_detail',order.customer.id)
   context = {
      'form': order_form,
      'order': order,
   }
   return render(request, 'products/updateOrder.html', context)

@login_required(login_url='customer:login')
def deleteOrder(request,id):
   context = {

   }
   return render(request, 'products/deleteOrder.html', context)