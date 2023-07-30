import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="HoangVanTu2102@", host="localhost", port=5432)

cursor = connection.cursor()

print(cursor)

# cursor.execute("SELECT * from account;")

# # Fetch all rows from database
# record = cursor.fetchall()

# print("Data from Database:- ", record)