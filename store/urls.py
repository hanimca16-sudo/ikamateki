from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/<str:residence>/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('inbox/', views.inbox, name='inbox'),
path('profile/', views.profile, name='profile'),
]