import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", dest = "input_file", default = '', help="Server name")
    parser.add_argument("-s", "--file_with_settings", dest = "file_with_settings", default = '', help="Server name")
    
    if parser.parse_args().input_file != '' and parser.parse_args().file_with_settings != '': 
        print(parser.parse_args())
        
    elif parser.parse_args().input_file != '':
        parser.error("Chose settings file!!! eg. -s settings.yaml")
        
    elif parser.parse_args().file_with_settings != '':
        parser.error("Chose input file for calculations!!! eg. -i CPMD_out_file.txt")
        
        
    else:
        import main_kivy
else: 
    raise(Exception("__name__ != '__main__', this program is not a module!!!"))