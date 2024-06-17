from weather.models import City
import pytest


pytestmark = pytest.mark.dependency()


def test_city_name_field_class():
    field = City._meta.get_field("name")
    assert field.__class__.__name__ == "CharField"


def test_city_name_field_max_length():
    field = City._meta.get_field("name")
    assert field.max_length == 60


def test_city_latitude_field_class():
    field = City._meta.get_field("latitude")
    assert field.__class__.__name__ == "FloatField"


def test_city_longitude_field_class():
    field = City._meta.get_field("longitude")
    assert field.__class__.__name__ == "FloatField"


def test_city_str_method(city):
    assert str(city) == "Belo Horizonte"


def test_city_slugify_method(city):
    assert city.slugify() == "belo-horizonte"


def test_city_save_method(db, city):
    city.save()
    assert city.name == "Belo Horizonte"


@pytest.mark.dependency(
    depends=[
        "test_city_save_method",
        "test_city_slugify_method",
        "test_city_str_method",
        "test_city_longitude_field_class",
        "test_city_latitude_field_class",
        "test_city_name_field_max_length",
        "test_city_name_field_class",
    ]
)
def test_city_model_final():
    pass
