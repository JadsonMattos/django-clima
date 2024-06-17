from pytest_django.asserts import assertTemplateUsed, assertContains
import pytest

pytestmark = pytest.mark.dependency()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "home.html")


def test_city_is_contained_in_home_page(client, city):
    response = client.get("/")
    assertContains(response, city)


@pytest.mark.dependency(
    depends=[
        "test_home_page",
        "test_city_is_contained_in_home_page",
    ]
)
def test_home_template_final():
    pass
