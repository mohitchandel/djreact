from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('blogs-api/', BlogListView.as_view()),
    path('blogs/<pk>', BlogListView.as_view())
]