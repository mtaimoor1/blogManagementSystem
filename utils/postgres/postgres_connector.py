import psycopg2
from psycopg2.extras import RealDictCursor


class Connector:

    def __init__(self, host, password, database, user):
        self.con = None
        self.host = host
        self.password = password
        self.database = database
        self.user = user

    @property
    def get_connection(self):
        if self.con:
            return self.con
        else:
            self.con = psycopg2.connect(host=self.host, database=self.database, user=self.user,
                                        password=self.password, cursor_factory=RealDictCursor)
            return self.con

