from django.urls import path
from . import views

urlpatterns = [
    path('posts/<str:residence>/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('add-post/', views.add_post, name='add_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
    path('send-message/<int:pk>/', views.send_message, name='send_message'),
]