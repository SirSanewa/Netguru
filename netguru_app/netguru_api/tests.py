from django.test import TestCase
from rest_framework.test import APIRequestFactory

from netguru_api.models import Car
from netguru_api.views import DeleteCars, Cars, PopularCars, RateCars


# Create your tests here.
class CarTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.new_car = Car.objects.create(make="Opel", model="Vectra")

    def test_show_cars(self):
        request = self.factory.get("/cars/")
        Cars(request=request)

    def test_add_car(self):
        request = self.factory.post("/cars/", {"make": "Volkswagen", "model": "Golf"})
        Cars(request=request)
