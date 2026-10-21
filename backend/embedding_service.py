# Import necessary libraries
from langchain_huggingface import HuggingFaceEmbeddings
import torch

#Import own librarys
from backend.classes.chunk import Chunk

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3", model_kwargs= {"device": "cuda" if torch.cuda.is_available() else "cpu"})

def create_embedding_for_chunk(chunks: list[Chunk]) -> list[Chunk]:
    """
        This function adds the embeddings for the content of one chunk.

        Args:
            A list of chunk object. Each object contains content which will be transformed into embeddings
        
        Return:
            The list with the chunks inclusive the embeddings
    """
    
    for chunk in chunks:
        chunk.embedding = embeddings.embed_query(chunk.chunk_content)
    
    return chunks

def create_embedding_for_query(query: str) -> list[float]:
    """
        Creates the embedding for the query of the user.

        Args: 
            The query as text.

        Return: 
            The embedding of the query text.
    """
    return embeddings.embed_query(query)