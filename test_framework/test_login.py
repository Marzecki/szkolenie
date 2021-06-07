import pytest
import requests
from hamcrest import *


@pytest.mark.parametrize('email, password, response', [('eve.holt@reqres.in', 'cityslicka', 200),
                                                       ('eve.holt@reqres.in', None, 400),
                                                       (None, 'eve.holt@reqres.in', 400),
                                                       ('test', 'test', 400)])
def test_login(email, password, response):
    body = {
        'email': email,
        'password': password
    }
    res = requests.post('https://reqres.in/api/login', data=body)
    print(f'response: {res.status_code}')
    assert res.status_code == response
    if response == 200:
        assert res.json()['token']


