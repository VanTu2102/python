import psycopg2


class Postgres:
    connection: any
    cursor: any
    database_name: str
    user: str
    password: str
    host: str
    port: int

    def __init__(self, database_name, user, password, host, port) -> None:
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(
            database=database_name, user=user, password=password, host=host, port=port)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

p = Postgres("postgres", 'hoangtu', 'HoangVanTu2102@', 'localhost', 5432)

# p.cursor.execute("CREATE TABLE IF NOT EXISTS your_table_name ( column1 integer, column2 bigint);INSERT INTO your_table_name VALUES (1,1092109);")
p.cursor.execute("DROP TABLE your_table_name;")
# p.cursor.execute("SELECT * from your_table_name;")

# Fetch all rows from database
# record = p.cursor.fetchall()

# print("Data from Database:- ", record)