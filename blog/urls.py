from django.urls import path
from . import views


urlpatterns = [

   #path('services/', views.services, name='services')
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name="category")
]