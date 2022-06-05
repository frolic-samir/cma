from django.shortcuts import redirect
from django.http import Http404,HttpResponse

def admin_only(view_func):
   def wrap_func(request,*args,**kwargs):
      group = request.user.groups.all().first()
      if group == None:
         return HttpResponse('Invalid user. You don\'t belong to any group. Identify yourself.')
      elif group.name == 'admin':
         return view_func(request,*args, **kwargs)
      elif group.name == 'customer':
         return redirect('products:customer_home')
   return wrap_func