# tests/test_projects.py
import httpx
from fastapi import status


def test_create_project(client):
    project_data = {"name": "Test Project", "description": "A test project"}
    response = client.post("/projects", json=project_data)

    assert response.status_code == 200
    assert response.json()["name"] == project_data["name"]
    assert response.json()["description"] == project_data["description"]

    client.delete(f'/projects/{response.json()["id"]}')


def test_get_project(client):
    response = client.get("/projects")
    assert response.status_code == 200


#
def test_update_project(client):
    project_data = {"name": "Test Project", "description": "A test project"}
    updated_project_data = {"name": "Test Project 2", "description": "An updated test project"}

    post_response = client.post("/projects", json=project_data)

    response = client.put(f'/projects/{post_response.json()["id"]}', json=updated_project_data)

    assert response.status_code == 200
    assert response.json()["name"] == updated_project_data["name"]
    assert response.json()["description"] == updated_project_data["description"]

    client.delete(f'/projects/{response.json()["id"]}')


#
def test_delete_project(client):
    project_data = {"name": "Test Project", "description": "A test project"}
    post_response = client.post("/projects", json=project_data)

    response = client.delete(f'/projects/{post_response.json()["id"]}')

    assert response.status_code == 200
    assert response.json()["name"] == project_data["name"]
    assert response.json()["description"] == project_data["description"]
