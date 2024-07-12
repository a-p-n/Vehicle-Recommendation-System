from django.urls import path
from . import views

urlpatterns = [
    path('random-car-list/', views.car_list, name='random_car_list'),
    path('select-car/', views.select_car, name='select_car'), 
]
