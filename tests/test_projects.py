# tests/test_projects.py
import httpx
from fastapi import status


def test_create_project(client):
    project_data = {"name": "Test Project", "description": "A test project"}
    response = client.post("/projects", json=project_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == project_data["name"]
    assert response.json()["description"] == project_data["description"]

# def test_get_project(client):
#     # TODO: Implement the get project test
#
# def test_update_project(client):
#     # TODO: Implement the update project test
#
# def test_delete_project(client):
#     # TODO: Implement the delete project test
