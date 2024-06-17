import pytest

try:
    from weather.models import City

    city_model_available = True
except ImportError:
    city_model_available = False

try:
    from weather.models import DailyWeather

    daily_weather_model_available = True
except ImportError:
    daily_weather_model_available = False

from datetime import date


@pytest.fixture
def city():
    if city_model_available:
        return City(
            name="Belo Horizonte", latitude=-23.5489, longitude=-46.6388
        )
    else:
        return None


@pytest.fixture
def daily_weather(city):
    if daily_weather_model_available:
        return DailyWeather(
            city=city,
            date=date.today(),
            min_temp=20.0,
            max_temp=30.0,
            brief_description="Ensolarado",
        )
    else:
        return None
