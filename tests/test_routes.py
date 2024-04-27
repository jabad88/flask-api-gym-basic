from app import app

def test_exercises_route():
    response = app.test_client().get('/exercises')
    assert response.status_code == 200

def test_can_create_exercise():
    pass