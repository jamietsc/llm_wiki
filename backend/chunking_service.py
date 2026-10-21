# Import nesessary libraries
from os import listdir
from os.path import isfile, join

#Import own modules
from backend.classes.chunk import Chunk

def get_filenames_in_directory(directory: str) -> list:
    """
    Get a list of filenames in the specified directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of filenames in the directory.
    """
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_read_files(path: str) -> str:
    """
    Get a string which is filled with the content of the file from the specified path.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_data_from_files() -> list:
    """
    Load the data from the files in the data directory and split it into chunks based on the "#" delimiter.
    After splitting clean the data sset by removing empty strings and whitespaces.

    Returns:
        list: A list of Chunk objects containing the chunked data.
    """
    chunks = []

    for file in get_filenames_in_directory("./data"):
        text = get_read_files(join("./data", file))
        for part in text.split("#"):
            part = part.strip()
            if part:
                x = Chunk(chunk_number=len(chunks)+1, chunk_content=part, source_file=file, path=join("./data", file))
                chunks.append(x)

    # Clean the data set by removing empty strings and whitespaces
    chunks = [chunk for chunk in chunks if chunk.chunk_content.strip()]

    return chunks