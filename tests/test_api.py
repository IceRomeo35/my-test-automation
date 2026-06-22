import requests

def test_get_post_status_code():
    """Verify that GET /posts/1 returns 200"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_post_has_required_fields():
    """Verify response contains userId and title"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    
    assert "userId" in data
    assert "title" in data

def test_create_post():
    """Verify POST request creates resource"""
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    assert response.status_code == 201
    assert response.json()["title"] == "foo"