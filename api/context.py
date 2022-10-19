import os
import yaml


class Context:
    def __init__(self):
        # reading configs
        with open(os.path.join(os.getcwd(), 'config.yaml'), 'r') as f:
            configs = yaml.safe_load(f)

        self.target_dir = configs['dir_name']


context = Context()
