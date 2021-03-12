import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from netguru_api.models import Car
from netguru_api.serializers import CarSerializer, RateSerializer


# Create your views here.
class Cars(APIView):
    """
    Allows user to create cars in database or display all available cars.
    """
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            make = serializer["make"].value
            model = serializer["model"].value
            r = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json")
            r_result = r.json()["Results"]
            if not Car.objects.filter(model=model):
                if filter(lambda x: x["Model_Name"] == model, r_result):
                    new_car = Car(make=make, model=model)
                    new_car.save()
                    return Response({"message": "Car created"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Car doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Car already exists in database"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        result = Car.objects.all()
        dict_result = list(map(lambda x: {"id": x.id, "make": x.make, "model": x.model, "avg_rating": round(x.avg_rating, 2)}, result))
        return Response({"Response": dict_result}, status=status.HTTP_202_ACCEPTED)


class DeleteCars(APIView):
    """
    Allows user to delete cars from database.
    """
    def delete(self, request, car_id):
        if car := Car.objects.filter(id=car_id):
            car.delete()
            return Response({"message": "Car deleted"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error": "Car of this id doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


class RateCars(APIView):
    """
    Allows user to rate cars from database.
    """
    def post(self, request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            car_id = serializer["car_id"].value
            rating = serializer["rating"].value
            car = Car.objects.get(pk=car_id)
            car.rates_number += 1
            if not car.avg_rating:
                car.avg_rating = rating
            else:
                new_avg_rating = ((car.avg_rating * car.rates_number - 1) + rating) / car.rates_number
                car.avg_rating = new_avg_rating
            car.save()
            return Response({"message": "Rating added"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopularCars(APIView):
    """
    Returns list of most popular cars, sorted by number of rates
    """
    def get(self, request):
        result = Car.objects.all().order_by("-rates_number")
        dict_result = list(map(lambda x: {"id": x.id, "make": x.make, "model": x.model, "rates_number": x.rates_number}, result))
        return Response({"Response": dict_result}, status=status.HTTP_202_ACCEPTED)

