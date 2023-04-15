import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_api_users():
    # Create an instance of the APIClient
    client = APIClient()

    r = client.get(
        f'/api/projects/',
        content_type='application/json',
        headers={'Authorization': f'Token 5c702bf51ab29f685c10c277918a6b9393f68a53'}
    )

    # Check if the API is working correctly
    assert r.status_code == 200
