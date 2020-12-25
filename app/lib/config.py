from pydantic import BaseSettings
import os

class Settings(BaseSettings):

    """ FastAPI configuration (docs) """
    app_slug: str = "file-storage-service"
    app_version: str = "0.0.1"
    app_description: str = "API service for file storage with token authentication."

    """ web server configuration """
    web_server: dict = {
        "allow_origins": ['*'],
        "allow_methods": ["*"],
        "allow_headers": ["*"]
    }

    """ service """
    length_of_random_file_name: int = 10
    output_directory: str = 'app/static'
    static_files: str = 'app/static'
    service_domain: str = os.environ.get('SERVICE_DOMAIN_NAME', 'www.yourdeployment.com')

    """ authentication """
    # todo encryption
    authentication: dict = {
        "domains": {
            "localhost:6900": 1
        },
        "tokens": {
            "XXX": 1
        }
    }

configuration = Settings()




