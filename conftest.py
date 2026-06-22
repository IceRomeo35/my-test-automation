import pytest
import requests

@pytest.fixture
def base_url():
    """Provides base URL for all tests"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client(base_url):
    """Provides a configured session"""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session, base_url