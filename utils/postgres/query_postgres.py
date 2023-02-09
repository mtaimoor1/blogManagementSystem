from postgres_connector import Connector
import os


postgres = Connector(host=os.environ.get("PG_HOST"), database=os.environ.get("PG_DATABASE"),
                     user=os.environ.get("PG_USER"), password=os.environ.get("PG_PASS"))


class QueryPG:

    def __init__(self):
        self.connection = postgres.get_connection
        self.cursor = self.connection.cursor()
