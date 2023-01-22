import yaml
from BondOrderCalculations import settings
import pprint


def perform_calculations(settings_file_path: str, input_file_path: str) -> None:
    """Perform calculations function
    
    Args:
        file_path (str): Path to file in ymal format with settings of calculations 
    """
    with open(settings_file_path, 'r') as file:
        yaml_data = file.read()

    with open(input_file_path, 'r') as file:
        input_file = file.read()
        
    data = yaml.safe_load(yaml_data)
    pprint.pprint(data)
    
    splited = input_file.split("\n")
    
    print(splited[1])
    
    #TODO 
    #Not done yet
    
    #settings_data = settings.Settings(data)
