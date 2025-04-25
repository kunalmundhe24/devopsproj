import pytest
import sys
import os

# Ensure the application path is included
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, notes  # Import the app and the notes list

@pytest.fixture
def client():
    """Creates a test client for Flask app."""
    app.config["TESTING"] = True
    client = app.test_client()
    
    # Clear notes before each test to ensure isolation
    notes.clear()

    yield client  # Return the test client for use in tests

def test_homepage(client):
    """Tests if the homepage loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Notes App" in response.data  # Updated to match new heading

def test_add_note(client):
    """Tests adding a new note."""
    response = client.post("/add", data={"content": "This is a test note"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"This is a test note" in response.data  # Ensure note appears on page

def test_delete_note(client):
    """Tests deleting a note."""
    # Add a note first
    client.post("/add", data={"content": "Note to be deleted"}, follow_redirects=True)

    # Delete the note (note_id=0 since it's the first one)
    response = client.get("/delete/0", follow_redirects=True)
    assert response.status_code == 200
    assert b"Note to be deleted" not in response.data  # Ensure it was deleted
