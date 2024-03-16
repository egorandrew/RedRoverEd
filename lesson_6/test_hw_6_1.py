import pytest
import requests

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'


@pytest.fixture(scope='module')
def get_auth():
    authdata = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=authdata)
    token = response.json()['token']
    print("====================================")
    assert response.status_code == 200
    yield token


@pytest.mark.smoke
def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200


def test_get_booking_by_id():
    response = requests.get(f"{base_url}/1")
    response_data = response.json()
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        'additionalneeds']
    print(response_data)
    assert response.status_code == 200
    assert len(expected_keys) == len(response_data.keys())
    for key in expected_keys:
        assert key in response_data.keys()


@pytest.fixture(scope='session')
def create_booking():
    payload = {
        "firstname": "Andrew",
        "lastname": "Egorov",
        "totalprice": 222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=payload)
    assert response.status_code == 200
    yield response.json()['bookingid']


@pytest.mark.xfail(reason="wrong")
def test_check_booking_id(create_booking):
    result = requests.get(f"{base_url}/{create_booking}")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == 'Andrew1'


def test_update_booking(get_auth, create_booking):
    playload = {
        "firstname": "Andrew1",
        "lastname": "Egorov1",
        "totalprice": 222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    token = {"Cookie": f"token={get_auth}"}
    response = requests.put(f"{base_url}/{create_booking}", json=playload, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f"{base_url}/{create_booking}")
    print(response_2.json())


def test_option():
    response = requests.head(f"{base_url}/1")
    assert response.status_code == 200
    print(response.headers)


def test_patch_booking(create_booking, get_auth):
    token = {"Cookie": f"token={get_auth}"}
    payload = {
        "firstname": "James"
    }
    response = requests.patch(f"{base_url}/{create_booking}", json=payload, headers=token)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['firstname'] == 'James'


def test_delete_booking(create_booking, get_auth):
    token = {"Cookie": f"token={get_auth}"}
    response = requests.delete(f"{base_url}/{create_booking}", headers=token)
    assert response.status_code == 201
    response_get = requests.get(f"{base_url}/{create_booking}")
    assert response_get.status_code == 404
