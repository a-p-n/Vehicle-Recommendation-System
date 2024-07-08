# car_recommendation/views.py
from django.shortcuts import render
from django.http import JsonResponse
from car_recommendation.models import Car
import random
from django.views.decorators.csrf import csrf_exempt
import json

def car_list(request):
    total_cars = Car.objects.count()
    random_indices = random.sample(range(total_cars), 20)
    random_cars = Car.objects.filter(id__in=random_indices)
    car_data = list(random_cars.values())

    return JsonResponse({'cars': car_data})


@csrf_exempt
def select_car(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            car_id = data.get('id')

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        
        if car_id:
            pass
        #     return JsonResponse({'status': 'success', 'message': f'Car ID {car_id} received.'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Invalid car ID.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)