# Import necessary libraries
from ollama import chat
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# Import own modules
from embedding_service import create_embedding_for_query
from database_service import load_cos_chunks_from_database
from routers.wiki_router import wiki_router

# Load the data from the files and split it into chunks
# chunks = get_data_from_files()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"], #allow http-methods
    allow_headers=["*"], #allow every header
)

@app.post("/ask")
def ask_query(query: dict):
    # Create the embeeding out of the query
    query_embedding = create_embedding_for_query(query["prompt"])

    # Load the matching chunk from the database
    chunks_from_db = load_cos_chunks_from_database(query_embedding)

    # Prepare the prompt for the LLM
    messages = [
        {
            "role": "system",
            "content": (
                "Du bist ein hilfsreicher KI-Assistent. "
                "Beantworte die Frage des Benutzers auf Deutsch **nur** basierend auf dem bereitgestellten Kontext. "
                "Nenne am Ende jeder Antwort immer die zugehörige Quelldatei (File) und den Pfad (Path). "
                "Wenn die Antwort nicht im Kontext enthalten ist, antworte exakt mit: "
                "'Leider gibt es zu dieser Frage keine passenden Antworten.'"
            )
        },
        {
            "role": "user",
            "content": f"Frage: {query['prompt']}\n\nKontext:\n" + "\n\n".join([
                f"Chunk {i+1}: {chunk.chunk_content}\nFile: {chunk.source_file}\nPath: {chunk.path}" 
                for i, chunk in enumerate(chunks_from_db)
            ])
        }
    ]

    print(messages[1]["content"])
    print("------------------------------------------")

    response = chat(model="qwen2.5:3b", messages=messages)

    print(type(response))
    print(response.message.content)

    return response.message.content

app.include_router(wiki_router)

# def main():
#     while True: 
#         # Get the user query and encode it
#         query = input("If you want to exit, type 'exit'. Enter your Question: ")

#         if query.lower() == "exit":
#             print("Exiting the program.")
#             break

#         query_embedding = create_embedding_for_query(query)

#         chunks_from_db = load_cos_chunks_from_database(query_embedding)

#         for chunk in chunks_from_db:
#             print(f"ID: {chunk.chunk_number}, Content: {chunk.chunk_content[:200]}, source File: {chunk.source_file}" )

#         messages = [
#             {
#                 "role": "user",
#                 "content": f"""Answer the following question in German based only on the provided context and add the source file and path of the answer.
#                 If the answer is not contained within the context, say 'Leider gibt es zu dieser Frage keine passenden Antworten ': {query}\n\nContext:\n""" + "\n\n".join([f"Chunk {i+1}: {chunk.chunk_content}, File: {chunk.source_file}, Path: {chunk.path}" for i, chunk in enumerate(chunks_from_db)])
#             }
#         ]

#         response = chat(model="qwen2.5:3b", messages=messages)

#         print(response.message.content)

# if __name__ == "__main__":
#     main()