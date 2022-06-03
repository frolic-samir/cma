from django.urls import path
from . import views as v

app_name = 'products'

urlpatterns =[
   path('', v.homeView, name='home'),
   path('products/', v.product_list, name='product_list'),
   path('product/add', v.add_product, name='add_product'),
   path('create_order/<str:id>/', v.createOrder, name='create_order'),
   path('update_order/<str:pk>/', v.updateOrder, name='update_order'),
   path('delete_order/<str:id>/', v.deleteOrder, name='delete_order'),
]