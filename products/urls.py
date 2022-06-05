from django.urls import path
from . import views as v

app_name = 'products'

urlpatterns =[
   path('', v.adminHomeView, name='admin_home'),
   path('ushop/', v.customerHomeView, name='customer_home'),
   path('products/', v.product_list, name='product_list'),
   path('product/add', v.add_product, name='add_product'),
   path('update_order/<str:pk>/', v.updateOrder, name='update_order'),
   
   path('create_order/', v.createOrder, name='create_order'),
   path('delete_order/<str:id>/', v.deleteOrder, name='delete_order'),
]