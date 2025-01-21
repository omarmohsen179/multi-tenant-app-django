import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

def get_database_settings():
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        return {
            'ENGINE': 'django_tenants.postgresql_backend',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': '5432',
        }
    
    # Parse database URL
    db_config = urlparse(database_url)
    
    return {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': db_config.path[1:],
        'USER': db_config.username,
        'PASSWORD': db_config.password,
        'HOST': db_config.hostname,
        'PORT': db_config.port or '5432',
    } 