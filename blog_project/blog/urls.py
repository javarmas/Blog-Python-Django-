# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<str:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
