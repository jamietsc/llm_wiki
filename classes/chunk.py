class Chunk:
    def __init__(self, chunk_number, chunk_content, source_file, path):
        self.chunk_number = chunk_number
        self.chunk_content = chunk_content
        self.source_file = source_file
        self.path = path