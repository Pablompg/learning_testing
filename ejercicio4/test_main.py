import pytest
from unittest.mock import patch
from datetime import datetime

from test_database_config import Base
from test_database_config import engine, client


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    # Create the tables
    Base.metadata.create_all(bind=engine)

    # Inject test data
    raw_conn = engine.raw_connection()
    with open("db/add_testing_data.sql", "r") as file:
        sql_script = file.read()
        raw_conn.executescript(sql_script)

    # Yield db
    yield

    # Drop all the tables
    Base.metadata.drop_all(bind=engine)


def test_authenticated_request(setup_test_db):
    response = client.post("/authenticate", json={"username": "raul", "password": "1234"})
    assert response.status_code == 200
    assert response.json() == {"Authentication": True}


def test_non_authenticated_request():
    response = client.post("/authenticate", json={"username": "POTATO", "password": "1234"})
    assert response.status_code == 401
    assert response.json() == {"detail": 'Incorrect username or password'}


@pytest.mark.skip(reason="remainingMinutesNonTestable endpoint is impossible to test")
@patch("main.datetime")
def test_remaining_minutes_in_year_non_testable(mock_datetime):
    specific_datetime = datetime(2023, 12, 31, 23, 0, 0)  # Dec 30, 2023, 15:00:00
    mock_datetime.now.return_value = specific_datetime

    # Make a request to the endpoint
    response = client.get("/remainingMinutesNonTestable")

    # Parse the response
    data = response.json()

    assert response.status_code == 200
    assert data["remaining_minutes"] == 60


@patch("main.get_current_date")
def test_remaining_minutes_in_year(get_current_date):
    specific_datetime = datetime(2023, 12, 31, 23, 0, 0)  # Dec 30, 2023, 15:00:00
    get_current_date.return_value = specific_datetime

    # Make a request to the endpoint
    response = client.get("/remainingMinutesTestable")

    # Parse the response
    data = response.json()

    assert response.status_code == 200
    assert data["remaining_minutes"] == 60
