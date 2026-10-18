from fastapi import APIRouter
from pathlib import Path

import data_service

wiki_router = APIRouter(
    prefix="/dict"
)

@wiki_router.get("/")
def api_get_data_directory():
    return data_service.get_folder_tree()

@wiki_router.post("/create_folder", status_code=201)
def api_create_new_folder(name: str, directory: str):
    return data_service.create_new_folder(name, directory)

