from os import listdir
from os.path import isfile, join
from sentence_transformers import SentenceTransformer, util
import torch

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
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

#Load the data from the files in the data directory and split it into chunks based on the "#" delimiter
chunks = []

for file in get_filenames_in_directory("./data"):
    text = get_read_files(join("./data", file))
    for part in text.split("#"):
        part = part.strip()
        if part:
            chunks.append(part)


# Clean the data set by removing empty strings and whitespaces
chunks = [cleaned for chunk in chunks if (cleaned := chunk.strip())]

# Load the model
model = SentenceTransformer("BAAI/bge-m3")

# Set the device to GPU if available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move the model to the selected device
model.to(device)

# Debug: Check which device is used for the model
# If it returns "True", it means the model is on GPU, otherwise it's on CPU
print(f"Model is using device: {next(model.parameters()).is_cuda}")

# create the vector out of the chunks
embeddings = model.encode(chunks, show_progress_bar=True)

# Get the user query and encode it
query = input("Enter your Question: ")
query_embedding = model.encode(query, show_progress_bar=True)

# Calculate the cosine similarity between the query and the chunks
cosine_scores = util.cos_sim(query_embedding, embeddings)

print("Cosine Similarity Scores:") 
print(cosine_scores)