from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('delete/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),

]
