import pytest

from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
    
def test_flag(client):
    resp = client.get('/history2')
    assert b'msfi{' in resp.data
