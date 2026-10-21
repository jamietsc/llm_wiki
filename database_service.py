# Import necessary libraries
import psycopg2
from pgvector import Vector

# Import own modules
from classes.config import settings
from classes.chunk import Chunk

def insert_chunks_into_database(chunk_list: list[Chunk]):
    """
    Insert the provided list of Chunk objects into the database.

    Args:
        chunk_list (list[Chunk]): A list of Chunk objects to be inserted into the database.
    """

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(f"dbname={settings.db_name} user={settings.db_user} password={settings.db_password}")
        cur = conn.cursor()

        # Insert each chunk into the database
        for chunk in chunk_list:
            cur.execute(
                "INSERT INTO items (embedding, chunk_content, source_file, path) VALUES (%s, %s, %s, %s)",
                (chunk.embedding, chunk.chunk_content, chunk.source_file, chunk.path)
            )

        # Commit the transaction and close the connection
        conn.commit()
    except Exception as e:
        print(f"An error occurred while inserting chunks into the database: {e}")
    finally: 
        close_database_connection(conn, cur)

def load_cos_chunks_from_database(query_embedding: list[float]) -> list[Chunk]:
    """
    Load all chunks from the database and return them as a list of Chunk objects.

    Returns:
        list[Chunk]: A list of Chunk objects retrieved from the database.
    """
    chunks = []
    conn = None
    cur = None

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(f"dbname={settings.db_name} user={settings.db_user} password={settings.db_password}")
        cur = conn.cursor()

        # Execute a query to get matching chunks from the database
        query = """
            WITH similarity_calculation AS (
                SELECT id, embedding, content, filename, filepath, 1 - (embedding <=> %s::vector) AS cos_similarity
                FROM items
                ORDER BY 1 - (embedding <=> %s::vector)
                LIMIT %s
            )
            SELECT id, embedding, content, filename, filepath
            FROM similarity_calculation
            WHERE cos_similarity > %s;
        """
        cur.execute(query, (query_embedding, query_embedding, settings.top_k_elements, settings.threshold))

        rows = cur.fetchall()

        # Create Chunk objects from the retrieved rows
        for row in rows:
            id, embedding, content, filename, filepath = row
            chunk = Chunk(chunk_number=id, embedding=embedding, chunk_content=content, source_file=filename, path=filepath)
            chunks.append(chunk)

    except Exception as e:
        print(f"An error occurred while loading chunks from the database: {e}")
        raise
    finally:
        close_database_connection(conn, cur)

    return chunks

def close_database_connection(conn, cur):
    """
    Close the database connection and cursor.

    Args:
        conn: The database connection object.
        cur: The database cursor object.
    """
    if cur:
        cur.close()
    if conn:
        conn.close()