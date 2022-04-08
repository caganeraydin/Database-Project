import os


def get_abs_filepath_from_module(module, relative_file_path):
    return os.path.abspath(os.path.join(os.path.dirname(module), relative_file_path))

