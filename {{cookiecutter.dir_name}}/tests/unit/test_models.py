"""
    Tests related to user database
"""

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated and role fields are correct
    """

    assert new_user.email == 'test@flask.com'
    assert new_user.role == 'user'
    assert new_user.check_password('test-password') is True