import os
from app.config import settings

def test_settings():
    # Set environment variables for testing
    os.environ['APP_NAME'] = 'TestApp'
    os.environ['APP_ENV'] = 'test'
    os.environ['APP_VERSION'] = '1.0.0'
    os.environ['HOST'] = '127.0.0.1'
    os.environ['PORT'] = '8000'
    os.environ['DEBUG'] = '1'
    os.environ['SECRET_KEY'] = 'testsecret'
    os.environ['POSTGRES_USER'] = 'testuser'
    os.environ['POSTGRES_PASSWORD'] = 'testpassword'
    os.environ['POSTGRES_HOST'] = 'localhost'
    os.environ['POSTGRES_PORT'] = '5432'
    os.environ['POSTGRES_DB'] = 'testdb'

    config = settings.__class__()

    assert config.APP_NAME == 'TestApp'
    assert config.APP_ENV == 'test'
    assert config.APP_VERSION == '1.0.0'
    assert config.HOST == '127.0.0.1'
    assert config.PORT == 8000
    assert config.DEBUG == True
    assert config.SECRET_KEY == 'testsecret'
    assert config.POSTGRES_USER == 'testuser'
    assert config.POSTGRES_PASSWORD == 'testpassword'
    assert config.POSTGRES_HOST == 'localhost'
    assert config.POSTGRES_PORT == '5432'
    assert config.POSTGRES_DB == 'testdb'