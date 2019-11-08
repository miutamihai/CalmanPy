from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.view_product, name='products'),
    path('calculate', views.calculate, name='calculate'),
]
