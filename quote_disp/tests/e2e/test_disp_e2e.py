from app import app

"""
    Check if we get the correct response for get '/get_quote'
    route and get the quote from the backend.
"""
def test_get_quote():
    with app.test_client() as c:
        response = c.get('/get_quote')
        assert response.status_code == 200
        assert b'<a class="link" href="https://youtube.com/@Hyperplexed" target="_blank"></a>' in response.data