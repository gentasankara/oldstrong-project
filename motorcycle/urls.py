from django.urls import path
from . import views

urlpatterns = [
    path('', views.motorcycle, name='motorcycle'),
    path('<int:id>', views.motorcycle_detail, name='motorcycle_detail'),
    path('search',views.search, name='search'), 
]
