import mysql.connector

try:
        def connect_to_db():
            return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Doctors"
        )
        print("Успешное подключение!")
except:
    print("Ошибка!")
