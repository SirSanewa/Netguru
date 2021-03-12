from django.urls import path
import netguru_api.views as api_view

urlpatterns = [
  path('cars/', api_view.Cars.as_view()),
  path('cars/<int:car_id>/', api_view.DeleteCars.as_view()),
  path('rate/', api_view.RateCars.as_view()),
  path('popular/', api_view.PopularCars.as_view())
]
