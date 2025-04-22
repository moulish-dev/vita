# vita/model_config.py

import yaml
import os

def load_model_configs():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    yaml_path = os.path.join(root_path, "models.yaml")

    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)
