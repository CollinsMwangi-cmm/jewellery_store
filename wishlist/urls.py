from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add-to-cart/', views.add_wishlist, name='add_to_wishlist'),
    path('delete/<int:product_id>/', views.delete_wishlist, name='delete_wishlist'),
    path('update/<int:product_id>/', views.update_wishlist, name='update_wishlist'),

]







