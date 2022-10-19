import os
import yaml


class Context:
    def __init__(self):
        self.BASE_DIR = os.getcwd()

        with open(os.path.join(self.BASE_DIR, 'config.yaml'), 'r') as f:
            configs = yaml.safe_load(f)

        self.target_dir = os.path.join(self.BASE_DIR, configs['dir_name'])


context = Context()
