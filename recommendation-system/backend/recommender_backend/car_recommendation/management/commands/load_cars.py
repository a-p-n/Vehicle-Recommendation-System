import csv
from django.core.management.base import BaseCommand
from car_recommendation.models import Car

class Command(BaseCommand):
    help = 'Load cars from CSV file'

    def handle(self, *args, **options):
        with open('../../../car.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['CONSUMER_RATING']:
                    consumer_rating = float(row['CONSUMER_RATING'])
                    Car.objects.create(
                        name=row['NAME'],
                        make=row['MAKE'],
                        model=row['MODEL'],
                        year=row['YEAR'],
                        mpg=row['MPG'],
                        transmission=row['TRANSMISSION'],
                        doors=row['DOORS'],
                        submodel=row['SUBMODEL'],
                        msrp=row['MSRP'],
                        rating=row['RATING'],
                        consumer_rating=consumer_rating,
                        photo=row['PHOTO']
                    )
