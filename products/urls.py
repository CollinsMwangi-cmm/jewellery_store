from django.urls import path
from . import views

urlpatterns = [
    path('chains/', views.chains , name='chains'),
    path('pendants/', views.pendants , name='pendants'),
    path('rings/', views.rings, name='rings'),
    path('bracelets/', views.bracelets, name='bracelets'),
    path('earrings/', views.earrings, name ='earrings'),
    path('grills/', views.grills, name='grills'),
    path('<int:product_id>/', views.product, name='product_detail'),
]
