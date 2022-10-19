import os
from api.context import context


class File:

    def __init__(self, file_name: str):
        file_path = os.path.join(context.target_dir, file_name)
        self.name: str = file_name
        self.type: str = 'file' if os.path.isfile(file_path) else 'folder'
        self.time: int = int(os.path.getctime(file_path))

    def serialize(self) -> dict[str, str | int]:
        return {
            'name': self.name,
            'type': self.type,
            'time': self.time
        }
