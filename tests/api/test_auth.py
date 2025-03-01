# Last modified: 2025-03-01 12:22:16 by Blackant222
from fastapi.testclient import TestClient
from app.core.security import create_access_token

def test_create_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "Test123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert "password" not in data

def test_login(client):
    # First create a user
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "logintest",
            "email": "login@example.com",
            "password": "Test123!"
        }
    )
    
    # Try to login
    response = client.post(
        "/api/v1/auth/token",
        data={
            "username": "logintest",
            "password": "Test123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"