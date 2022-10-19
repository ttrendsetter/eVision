import os
from api.context import context


def get_folder_info():
    """
    Returns info about files in a folder pointed in config.yaml
    """
    result = []
    for file in os.listdir(context.target_dir):
        file_path = os.path.join(context.target_dir, file)
        result.append({
            'name': file,
            # Getting the type of current file
            'type': 'file' if os.path.isfile(file_path) else 'folder',
            # Getting the file creation time
            'time': int(os.path.getctime(file_path))

        })
    return result
