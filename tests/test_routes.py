from app import app

#Question: Do i run coverage commands in the tests folder or in the root dir?

def test_exercises_route():
    response = app.test_client().get('/exercises')
    assert response.status_code == 200
    assert response is not None

def test_can_create_exercise():
    payload = {
        "name": "new exercise"
    }
    response = app.test_client().post('/exercises', json=payload)
    assert response.status_code == 201

    print(response.json)



