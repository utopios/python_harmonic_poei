def test_post_correct_product_should_reponse_200(client,get_jwt):
    response = client.post('/products', json={'title': 'demo-product', 'price': 100, 'stock':100}, headers={'Authorization': 'Bearer '+get_jwt})
    assert response.status_code == 200

def test_post_correct_product_response_should_be_json(client):
    response = client.post('/products', json={'title': 'demo-product', 'price': 100, 'stock':100})
    assert response.is_json == True


def test_get_products_response_should_be_list(client):
    response = client.get('/products')
    assert isinstance(response.json, list)

def test_get_product__with_correct_id_response_should_be_json(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.is_json == True

def test_get_product__with__id_response_should_be_json(client):
    response = client.get('/products/100')
    result = response.json
    assert response.status_code == 404