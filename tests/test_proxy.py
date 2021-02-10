import pytest

from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_bad_parameter(client):
    data = {'i_want_the_flag': 'no'}
    resp = client.post('/intercept', data=data)
    assert b'msfi{' not in resp.data
    
def test_good_parameter(client):
    data = {'i_want_the_flag': 'yes'}
    resp = client.post('/intercept', data=data)
    assert b'msfi{' in resp.data
