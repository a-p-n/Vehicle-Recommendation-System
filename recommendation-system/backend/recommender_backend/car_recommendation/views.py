# car_recommendation/views.py
from django.shortcuts import render
from django.http import JsonResponse
from car_recommendation.models import Car
import random

def car_list(request):
    total_cars = Car.objects.count()
    random_indices = random.sample(range(total_cars), 20)
    random_cars = Car.objects.filter(id__in=random_indices)
    car_data = list(random_cars.values())
    
    return JsonResponse({'cars': car_data})
