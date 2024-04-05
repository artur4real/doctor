from database.connection import connect_to_db

def insert_doctors_data(doctors_data):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "INSERT INTO Doctors(FirstName, LastName, Specialty, ExperienceYears, Email) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, doctors_data)

    conn.commit()
    cursor.close()
    conn.close()
