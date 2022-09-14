from app_factory import app_factory


def test_post_simple_resource_correct_value_status_code_200():
    """When post request with email value the status code should be 200"""
    ##Arrange
    app = app_factory({'MODE': 'DEBUG', 'DATABASE_URI': 'postgresql://cours:db@localhost:5431/demo_harmonic'})
    with app.test_client() as client:
        response = client.post('/simple', json={'email': 'demo@demo.fr'}, headers={'Authorization': 'Bearer '})
        assert response.status_code == 200
