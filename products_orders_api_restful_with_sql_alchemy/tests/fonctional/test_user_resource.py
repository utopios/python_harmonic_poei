def test_save_correct_user_shoud_return_200(client):
    response = client.post('/users', json={'email': 'ihab@utopios.net', 'password':'123456789', 'role':'admin'})
    assert response.status_code == 200
    assert response.is_json == True


def test_login_correct_user_sould_return_string(client):
    response = client.post('/users/login', json={'email': 'ihab@utopios.net', 'password':'123456789'})
    assert response.status_code == 200
    assert isinstance(response.json, str)