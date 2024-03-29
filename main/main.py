import argparse
from multiprocessing import freeze_support
import time

if __name__ == '__main__':
    # Add support for when a program which uses multiprocessing has been frozen to produce a Windows executable
    freeze_support()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file",
                        dest="input_file", default='', help="input file")
    parser.add_argument("-s", "--file_with_settings",
                        dest="file_with_settings", default='', help="file with settings")
    parser.add_argument("-o", "--output_file",
                        dest="output_file", default='output.txt', help="output_file")

    if parser.parse_args().input_file != ''\
            and parser.parse_args().file_with_settings != '':
        start = time.time()
        from app_back_end import AppBackEnd

        data = parser.parse_args()

        app_for_cli = AppBackEnd(False)
        app_for_cli.load_data(data.input_file)
        app_for_cli.load_settings(data.file_with_settings)
        app_for_cli.perform_calculations()
        app_for_cli.save_output(data.output_file)
        end = time.time()
        print(f"Done!, execution time: {end - start} s")

    elif parser.parse_args().input_file != '':
        parser.error("Chose settings file!!! eg. -s settings.yaml")

    elif parser.parse_args().file_with_settings != '':
        parser.error(
            "Chose input file for calculations!!! eg. -i CPMD_out_file.txt")

    else:
        import main_kivy
        main_kivy.run_app()
