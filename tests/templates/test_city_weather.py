from pytest_django.asserts import assertTemplateUsed, assertContains
import pytest

pytestmark = pytest.mark.dependency()


def test_city_weather_page(client, city):
    response = client.get(f"/weather/{city.slugify()}")
    assert response.status_code == 200
    assertTemplateUsed(response, "city_weather.html")


def test_correct_weather_is_contained_in_home_page(
    client, city, daily_weather
):
    response = client.get(f"/weather/{city.slugify()}")
    assertContains(response, daily_weather)


@pytest.mark.dependency(
    depends=[
        "test_city_weather_page",
        "test_correct_weather_is_contained_in_home_page",
    ]
)
def test_city_weather_template_final():
    pass
