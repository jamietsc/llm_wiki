from os import listdir
from os.path import isfile, join

def get_filenames_in_directory(directory):
    """
    Get a list of filenames in the specified directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of filenames in the directory.
    """
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_read_files(path):
    """
    Get a string which is filled with the content of the file from the specified path.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(path, 'r') as f:
        return f.read()


files = get_filenames_in_directory('./data')

for file in files:
    print(f'File: {get_read_files(f"./data/{file}")}')
    break