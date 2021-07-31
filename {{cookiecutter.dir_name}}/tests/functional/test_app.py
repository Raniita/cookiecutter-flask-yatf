"""
    Tests releated to redirects on webpage
"""

def test_index(test_client):
    response = test_client.get("/")

    # Redirect to login (user not authenticated)
    assert response.status_code == 302
    assert b'/login' in response.data

def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask aplication
    WHEN the '/login' paga is posted to (POST)
    THEN check the response is valid
    """

    response = test_client.post('/login', 
                                data=dict(email="admin@flask.com",
                                          password="admin_password",
                                          follow_redirects=True))
    
    # Redirect to '/dashboard'
    assert response.status_code == 302
    assert b'/dashboard' in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """

    response = test_client.get('/logout',
                               follow_redirects=True)
    
    # Redirect to '/login'
    assert response.status_code == 200
    assert b'/login' in response.data