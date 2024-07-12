# car_recommendation/views.py
from django.shortcuts import render
from django.http import JsonResponse
from car_recommendation.models import Car
import random
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd
import pickle
import os


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
            df = pd.read_csv('../../cars.csv')
            cosine_sim = pd.read_pickle("../../cosine_sim.pkl")
            def get_content_recommendations(item_index, num_recommendations=25):
                similarity_scores = list(enumerate(cosine_sim[item_index]))
                similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
                similarity_scores = similarity_scores[1:num_recommendations+1]
                item_indices = [i[0] for i in similarity_scores]
                return df.iloc[item_indices]
            rec = get_content_recommendations(car_id)
            rec = rec.tail(5)
            rec = rec.fillna("-")
            recommendations = rec.to_dict(orient='records')
            return JsonResponse({'status': 'success', 'recommendations': recommendations})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid car ID.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)