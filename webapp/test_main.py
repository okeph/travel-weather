from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    expected_countries = ["England", "France", "Germany", "Italy", "Peru",
                          "Portugal", "Spain"]
    assert sorted(response.json()) == expected_countries
