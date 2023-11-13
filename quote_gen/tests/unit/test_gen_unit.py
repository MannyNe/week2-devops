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
    assert b'<h1 style="color: white">Quote Generation Service</h1>' in response.data


"""
    Check if the web displays the correct information
    on the get '/' request.
"""
def test_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    ]
    response = app.test_client().get('/quote')
    assert response.status_code == 200
    assert response.get_data(as_text=True) in quotes
