import psycopg2

class Postgres:
    connection: any
    cursor: any
    database_name: str
    user: str
    password: str
    host: str
    port: int

    def __init__(self, database_name, user, password, host, port, autocommit) -> None:
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(
            database=database_name, user=user, password=password, host=host, port=port)
        self.connection.autocommit = autocommit
        self.cursor = self.connection.cursor()

    def excute_query_get(self, query):
        self.cursor.execute(query=query)
        return self.cursor.fetchall()
    
    def excute_query_update(self, query):
        self.cursor.execute(query=query)
        return self.connection.commit()

    def disconnect(self):
        self.connection.close()