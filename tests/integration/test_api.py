from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_generate_content():
    response = client.post("/generate", json={"prompt": "Hello", "max_length": 10})
    assert response.status_code == 200
    assert "generated_text" in response.json()
    