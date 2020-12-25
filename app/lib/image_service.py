import base64
from mimetypes import guess_extension, guess_type
from app.lib.config import configuration
import string
import random
import pathlib

def get_random_string(length_of_output=10):
    """
    Generate an output String that consists of random alphabetical characters
    with a length of {length_of_output} characters.
    """
    letters = string.ascii_letters
    return (''.join(random.choice(letters) for i in range(length_of_output)))

def base64_to_url(data, client_id):
    """
    Takes a base64 encoded string, save to storage
    Returns a URL where an image can be accessed.
    """
    file_name = data.get('file_name', f"{get_random_string()}{guess_extension(guess_type(data.get('base64_encoded', []))[0])}")
    file = bytes(data.get('base64_encoded', ',').split(',')[1].encode('utf-8'))

    pathlib.Path(f"{configuration.output_directory}/{client_id}").mkdir(parents=True, exist_ok=True)

    directory = ''
    if '/' in file_name:
        slash_delimited = file_name.split('/')
        file_name = slash_delimited[-1]
        directory = '/'.join(slash_delimited[:-1])
        pathlib.Path(f"{configuration.output_directory}/{client_id}{directory}").mkdir(parents=True, exist_ok=True)

    full_path = f"{client_id}{directory}/{file_name}"

    with open(f"{configuration.output_directory}/{full_path}", "wb") as fh:
        fh.write(base64.decodebytes(file))

    return full_path

