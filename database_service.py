# Import necessary libraries
import psycopg2

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
        conn = psycopg2.connect(f"dbname={settings.dbname} user={settings.db_user} password={settings.db_password}")
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

def load_chunks_from_database() -> list[Chunk]:
    """
    Load all chunks from the database and return them as a list of Chunk objects.

    Returns:
        list[Chunk]: A list of Chunk objects retrieved from the database.
    """
    chunks = []
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(f"dbname={settings.dbname} user={settings.db_user} password={settings.db_password}")
        cur = conn.cursor()

        # Execute a query to retrieve all chunks from the database
        cur.execute("SELECT id, embedding, chunk_content, source_file, path FROM items")
        rows = cur.fetchall()

        # Create Chunk objects from the retrieved rows
        for row in rows:
            id, embedding, chunk_content, source_file, path = row
            chunk = Chunk(chunk_number=id, embedding=embedding, chunk_content=chunk_content, source_file=source_file, path=path)
            chunks.append(chunk)

    except Exception as e:
        print(f"An error occurred while loading chunks from the database: {e}")
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