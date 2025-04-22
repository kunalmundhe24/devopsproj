import pytest
import sys
import os

# Ensure the application path is included
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Ensure 'app.py' is detected

@pytest.fixture
def client():
    """Creates a test client for Flask app."""
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False  # Disable CSRF for testing if applicable
    client = app.test_client()
    yield client  # Return the client for testing

def test_homepage(client):
    """Tests if the homepage loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List" in response.data  # Check if "To-Do List" exists in response

def test_add_task(client):
    """Tests adding a new task."""
    response = client.post("/add", data={"content": "Buy groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" in response.data  # Ensure task appears on page

def test_delete_task(client):
    """Tests deleting a task."""
    client.post("/add", data={"content": "Test Task"}, follow_redirects=True)

    # Fetch task list to get the correct ID
    response = client.get("/")
    assert b"Test Task" in response.data  # Ensure it was added

    # Assuming tasks are displayed in a certain structure, extract the first task ID (modify if needed)
    task_id = 1  # Modify this based on how your tasks are stored
    response = client.get(f"/delete/{task_id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" not in response.data  # Ensure task was removed
