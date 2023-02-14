from .postgres_connector import Connector
import os
from schema.schema import Post

postgres = Connector(host=os.environ.get("PG_HOST"), database=os.environ.get("PG_DATABASE"),
                     user=os.environ.get("PG_USER"), password=os.environ.get("PG_PASS"))


class QueryPG:

    def __init__(self):
        self.connection = postgres.get_connection
        self.cursor = self.connection.cursor()

    def get_posts(self, table: str, post_id: str = None):
        if post_id:
            query = """
                    SELECT * FROM %s WHERE id=%s
                    """%(table, post_id)
        else:
            query = """SELECT * FROM %s"""%(table)
        self.cursor.execute(f"{query}")
        data = self.cursor.fetchall()
        return data

    def insert_post(self, post: Post):
        self.cursor.execute(""" INSERT INTO posts (title,body,rating,published) 
                            VALUES (%s, %s, %s, %s) RETURNING *""",
                            (post.title, post.body, post.rating, post.published))
        data = self.cursor.fetchone()
        self.connection.commit()
        return data
