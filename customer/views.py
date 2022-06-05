from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .filter import FilterQuerySet
from .forms import CustomerProfile, CreateUserForm, CustomerProfileForm, SignInForm
from products.forms import SearchOrderForm

def register(request):
   form = CreateUserForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('customer:login')
   context={
      'form':form
   }
   return render(request, 'accounts/register.html', context)

def signIn(request):
   form = SignInForm(request.POST or None)
   if form.is_valid():
      data = form.cleaned_data
      user = authenticate(username=data['username'],password=data['password'])
      if user is not None:
         login(request,user)
         return redirect('products:admin_home')
      else:
         messages.error(request,"Invalid user")
   context = {
      'form': form,
   }
   return render(request, 'accounts/login.html', context)

def signOut(request):
   logout(request)
   return redirect('customer:login')

def customer_detail(request,customer_id):
   customer = get_object_or_404(CustomerProfile,id=customer_id)
   orders = customer.order_set.all()
   order_count = orders.count()
   search_form = SearchOrderForm()
   
   if request.GET.get('refresh'):
      orders=orders
   elif request.GET.get('product') or request.GET.get('status'):
      search_obj=FilterQuerySet(
         product =request.GET.get('product'),
         status = request.GET.get('status'),
         orders_qs=orders )
      orders=search_obj.querySearch()
      search_form=SearchOrderForm(initial={'product':request.GET.get('product'), 'status':request.GET.get('status')})

   context={
      'customer':customer,
      'orders':orders,
      'order_count':order_count,
      'form':search_form,
   }
   return render(request,'accounts/customers.html', context)

def customerProfile(request):
   user = request.user.customerprofile
   form = CustomerProfileForm(instance=user)
   if request.method == 'POST':
      form = CustomerProfileForm(request.POST, request.FILES, instance=user)
      if form.is_valid():
         print(form.cleaned_data)
         form.save()

   context={
      'form':form,
   }
   return render(request, 'accounts/customer_profile.html', context)