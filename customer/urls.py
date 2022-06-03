from django.urls import path
from . import views as v
from django.contrib.auth import views as auth_view

app_name = 'customer'

urlpatterns =[
     path('register/', v.register, name='register'),
     path('login/', v.signIn, name='login'),
     path('logout/', v.signOut, name='logout'),
     path('reset_password/', auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
          name='password_reset'),
     path('reset_password/done/', auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
          name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
          name='password_reset_confirm'),
     path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),
          name='password_reset_complete'),

     path('customer/<int:customer_id>/', v.customer_detail, name='customer_detail'),
]