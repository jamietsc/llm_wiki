# Import nessecary libraries
from fastapi import FastAPI, HTTPException
from os import listdir
from os.path import isfile, join
import os
import json
from pathlib import Path


app = FastAPI()

DATA_DIR = Path(__file__).resolve().parent / "data"

def get_folder_tree(directory: Path = DATA_DIR):
    """
        Get a list of every item in the directory

        Args: 
            directory (Path): The path of the directory

        Returns:
            A list of items in the directory
    """
    return {
        "name": directory.name,
        "type": "folder",
        "children": [
            get_folder_tree(item) if item.is_dir()
            else {"name": item.name, "type": "file"}
            for item in sorted(directory.iterdir())
        ],
    }

def create_new_folder(name: str, directory: str):
    """
        Function creates a new folder in the given directory

        Args:
            name (str): the name of the new directory
            directory (Path): the path where the folder will be created.
    """
    if name == "":
        raise HTTPException(status_code=400, detail="The name of the folder can not be empty.")

    full_path = os.path.join(directory, name)

    if not os.path.exists(full_path):
        os.mkdir(full_path)
        return {
            "path": full_path, 
            "status": "created", 
            "detail": "Successfull created the new folder."
        }
    else:
        return {
            "path": full_path, 
            "status": "already exists", 
            "detail": "The folder already exists in the selected Path."
        }

def delete_folder(path: str):
    """
        Function deletes a folder in the given path

        Args:
            path (str): This is the path of the folder
    """

    if path == "":
        raise HTTPException(status_code=400, detail="The path of the folder can't be empty.")

    if os.path.exists(path):
        os.rmdir(path)
        return {
            "path": path,
            "status": "deleted",
            "detail": "Successfull deleted the selected Folder"
        }
    else:
        raise HTTPException(status_code=400, detail="The folder you're trying to delete doesn't exists.")


