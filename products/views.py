from django.shortcuts import render, get_object_or_404, redirect

from customer.models import CustomerProfile
from .forms import UpdateOrderForm, ProductAddForm
from .models import Product, Order

# Create your views here.

def homeView(request):
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

def product_list(request):
   products = Product.objects.all()
   context = {
      'products':products,
   }
   return render(request, 'products/products.html', context)

def add_product(request):
   form = ProductAddForm(request.POST or None)
   if form.is_valid():
      print(form.cleaned_data)
      form.save()
      return redirect('products:product_list')
   context = {
      'form':form
   }
   return render(request, 'products/add_product.html', context)

def createOrder(request,id):
   context = {

   }
   return render(request, 'products/orderForm.html', context)

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

def deleteOrder(request,id):
   context = {

   }
   return render(request, 'products/deleteOrder.html', context)