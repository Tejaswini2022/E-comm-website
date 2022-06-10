from django.urls import path
from . import views

urlpatterns = [

   path('', views.products, name="products"),
   path('<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
   #path('cart/', views.cart, name="cart"),

]