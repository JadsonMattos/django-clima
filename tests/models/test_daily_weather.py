from weather.models import DailyWeather
from datetime import date
import pytest

pytestmark = pytest.mark.dependency()


def test_daily_weather_city_field_class():
    field = DailyWeather._meta.get_field("city")
    assert field.__class__.__name__ == "ForeignKey"


def test_daily_weather_city_field_unique_for_date():
    field = DailyWeather._meta.get_field("city")
    assert field.unique_for_date == "date"


def test_daily_weather_date_field_class():
    field = DailyWeather._meta.get_field("date")
    assert field.__class__.__name__ == "DateField"


def test_daily_weather_min_temp_field_class():
    field = DailyWeather._meta.get_field("min_temp")
    assert field.__class__.__name__ == "FloatField"


def test_daily_weather_max_temp_field_class():
    field = DailyWeather._meta.get_field("max_temp")
    assert field.__class__.__name__ == "FloatField"


def test_daily_weather_brief_description_field_class():
    field = DailyWeather._meta.get_field("brief_description")
    assert field.__class__.__name__ == "CharField"


def test_daily_weather_brief_description_field_max_length():
    field = DailyWeather._meta.get_field("brief_description")
    assert field.max_length == 20


def test_daily_weather_brief_description_field_choices():
    field = DailyWeather._meta.get_field("brief_description")
    choices_set = set([choice for choice, _ in field.choices])
    assert choices_set == set(
        [
            "Ensolarado",
            "Chuvoso",
            "Nublado",
            "Parcialmente nublado",
            "Neve",
            "Granizo",
        ]
    )


def test_daily_weather_str_method(daily_weather):
    assert (
        str(daily_weather)
        == f"{date.today().strftime('%d/%m/%Y')} - Ensolarado"
    )


@pytest.mark.dependency(
    depends=[
        "test_daily_weather_city_field_class",
        "test_daily_weather_city_field_unique_for_date",
        "test_daily_weather_date_field_class",
        "test_daily_weather_min_temp_field_class",
        "test_daily_weather_max_temp_field_class",
        "test_daily_weather_brief_description_field_class",
        "test_daily_weather_brief_description_field_max_length",
        "test_daily_weather_brief_description_field_choices",
        "test_daily_weather_str_method",
    ]
)
def test_daily_weather_model_final():
    pass
