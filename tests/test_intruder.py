import pytest

from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_bad_method(client):
    resp = client.get('/intruder.json')
    assert resp.status_code == 405
    assert b'msfi{' not in resp.data 
    resp = client.post('/intruder.json')
    assert resp.status_code == 405
    assert b'msfi{' not in resp.data 


def test_bad_form(client):
    d = {'key': 0}
    resp = client.put('/intruder.json', data=json.dumps(d))
    assert resp.status_code == 400
    assert b'msfi{' not in resp.data 

def test_bad_key(client):
    d = {'key': 1}
    headers = {
        'Content-Type': 'application/json'
    }
    resp = client.put('/intruder.json', data=json.dumps(d), headers=headers)
    assert b'not the correct key' in resp.data 
    assert b'msfi{' not in resp.data 

def test_json_without_key(client):
    d = {'ke': 1}
    headers = {
        'Content-Type': 'application/json'
    }
    resp = client.put('/intruder.json', data=json.dumps(d), headers=headers)
    assert b'I want the key' in resp.data 
    assert b'msfi{' not in resp.data 

def test_valid_request(client):
    d = {'key': 2}
    headers = {
        'Content-Type': 'application/json'
    }
    resp = client.put('/intruder.json', data=json.dumps(d), headers=headers)
    assert b'msfi{' in resp.data 