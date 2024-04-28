from app import app
#Question: Do i run coverage commands in the tests folder or in the root dir?


def test_exercises_route():
    response = app.test_client().get('/exercises')
    assert response.status_code == 200
    assert response is not None

def test_can_create_exercise():
    payload = {
        "name": "new exercise1"
    }
    response = app.test_client().post('/exercises', json=payload)
    assert response.status_code == 201

    # print(response.json)

def test_get_single_exercise():
    response = app.test_client().get('/1')
    print(response.json)
 
    assert response.json['id'] == 1
    assert response.json['name'] == 'bench press'
    assert response.status_code == 200

    response = app.test_client().get('/3') 
    print(response.json)

    assert response.json['id'] == 3
    assert response.json['name'] == 'squat'
    assert response.status_code == 200

    response = app.test_client().get('/54') 
    print(response.json)

    assert response.json['id'] == 54
    assert response.json['name'] == 'update 54 using pytest'
    assert response.status_code == 200

def test_update_exercise():
    payload = {"name": 'update 54 using pytest'}

    response = app.test_client().put("/54", json=payload)
    
    assert response.json['id'] == 54
    assert response.json['name'] == payload['name']
    assert response.status_code == 200
    print(response.json)


