from app import app

"""
    Check if health endpoint is working correct on
    get '/health'
"""
def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data


"""
    Check if the web displays the correct information
    on the get '/' request.
"""
def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'This is the Quote Display Service' in response.data
