from django.urls import path
from weather.views import city_weather, weather_details, index


urlpatterns = [
    path("", index, name="homepage"),
    path("weather/<str:city>", city_weather, name="city_weather"),
    path("weather/<str:city>/<str:target>", weather_details,
         name="weather_details")
]
