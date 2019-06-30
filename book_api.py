import os
from app import create_app

env_name = os.getenv('FLASK_ENV', 'default')

app = create_app(env_name)

