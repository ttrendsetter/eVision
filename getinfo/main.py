import os
from api.context import context
from .classes import File


def get_folder_info():
    """
    Returns info about files in folder chosen in config.yaml
    """
    result = []
    for file in os.listdir(context.target_dir):
        result.append(File(file).serialize())
    return result
