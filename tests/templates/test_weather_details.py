from pytest_django.asserts import assertTemplateUsed, assertContains
import pytest

pytestmark = pytest.mark.dependency()


def test_weather_details_page(client, city, daily_weather):
    response = client.get(
        f"/weather/{city.slugify()}/{daily_weather.date.strftime('%Y-%m-%d')}"
    )
    assert response.status_code == 200
    assertTemplateUsed(response, "weather_details.html")


def test_correct_weather_description_is_contained_in_weather_details_page(
    client, city, daily_weather
):
    response = client.get(
        f"/weather/{city.slugify()}/{daily_weather.date.strftime('%Y-%m-%d')}"
    )
    assertContains(response, daily_weather.brief_description)


@pytest.mark.dependency(
    depends=[
        "test_weather_details_page",
        (
            "test_correct_weather_description_"
            "is_contained_in_weather_details_page"
        ),
    ]
)
def test_weather_details_template_final():
    pass
