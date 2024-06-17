from django.shortcuts import render
from weather.models import City, DailyWeather
from datetime import date


def index(request):
    context = {'cities': City.objects.all()}
    return render(request, 'home.html', context)


def city_weather(request, city):
    deslugified_city = city.replace('-', ' ').title()

    queried_city = City.objects.get(name=deslugified_city)

    weathers = DailyWeather.objects.filter(city=queried_city)

    context = {'city': queried_city, 'weathers': weathers}
    return render(request, 'city_weather.html', context)


def weather_details(request, city, target):
    deslugified_city = city.replace('-', ' ').title()

    target_date = date.fromisoformat(target)

    queried_city = City.objects.get(name=deslugified_city)

    queried_weather = DailyWeather.objects.get(
        city=queried_city,
        date=target_date
    )

    context = {'weather': queried_weather}
    return render(request, 'weather_details.html', context)
