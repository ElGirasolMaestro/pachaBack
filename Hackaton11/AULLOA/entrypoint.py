import os
from app import create_app


settings_module = "config.dev"# os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)