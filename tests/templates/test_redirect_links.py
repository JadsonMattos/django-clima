from pytest_django.asserts import assertContains
import pytest

pytestmark = pytest.mark.dependency()


def test_home_page_contains_city_link(client, city):
    response = client.get("/")
    assertContains(response, f'href="/weather/{city.slugify()}"')


def test_city_weather_page_contains_weather_link(client, city, daily_weather):
    response = client.get(f"/weather/{city.slugify()}")
    assertContains(
        response,
        (
            f'href="/weather/{city.slugify()}/'
            f'{daily_weather.date.strftime("%Y-%m-%d")}"'
        ),
    )


def test_city_weather_page_contains_back_link(client, city):
    response = client.get(f"/weather/{city.slugify()}")
    assertContains(
        response,
        'href="/',
    )


def test_weather_details_page_contains_back_link(client, city):
    response = client.get(f"/weather/{city.slugify()}")
    assertContains(
        response,
        f'href="/weather/{city.slugify()}/',
    )


@pytest.mark.dependency(
    depends=[
        "test_home_page_contains_city_link",
        "test_city_weather_page_contains_weather_link",
        "test_city_weather_page_contains_back_link",
        "test_weather_details_page_contains_back_link",
    ]
)
def test_redirect_links_in_templates_final():
    pass
