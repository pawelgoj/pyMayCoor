import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file",
                        dest="input_file", default='', help="input file")
    parser.add_argument("-s", "--file_with_settings",
                        dest="file_with_settings", default='', help="file with settings")
    parser.add_argument("-o", "--output_file",
                        dest="output_file", default='output.txt', help="output_file")

    if parser.parse_args().input_file != ''\
            and parser.parse_args().file_with_settings != '':

        from main_cli import AppForCli

        data = parser.parse_args()

        app_for_cli = AppForCli(
            data.file_with_settings, data.input_file, data.output_file)

        app_for_cli.perform_calculations()
        app_for_cli.save_output()

    elif parser.parse_args().input_file != '':
        parser.error("Chose settings file!!! eg. -s settings.yaml")

    elif parser.parse_args().file_with_settings != '':
        parser.error(
            "Chose input file for calculations!!! eg. -i CPMD_out_file.txt")

    else:
        import main_kivy
else:
    raise (Exception("__name__ != '__main__', this program is not a module!!!"))
