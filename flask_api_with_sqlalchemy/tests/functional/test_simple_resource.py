from app import app


def test_post_simple_resource_correct_value_status_code_200():
    """When post request with email value the status code should be 200"""
    with app.test_client() as client:
        response = client.post('/simple', json={'email': 'demo@demo.fr'})
        assert response.status_code == 200
