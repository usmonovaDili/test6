from django.urls import path
from .views import blog_list, blog_all

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('blog/',blog_all, name='blog_all')
]
