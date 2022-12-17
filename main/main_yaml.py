import yaml
from BondOrderCalculations import settings


def perform_calculations(file_path: str) -> None:
    with open(file_path, 'r') as file:
        yaml_data = file.read()

    data = yaml.safe_load(yaml_data)
    settings_data = settings.Settings(data)
