import mysql.connector

# Connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your host if needed
            user='root',       # Replace with your MySQL username
            password='123456',  # Replace with your MySQL password
            database='student_db'  # Database name created earlier
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Insert a new student into the database
def insert_student(first_name, last_name, age, major):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO students (first_name, last_name, age, major) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, age, major)
        cursor.execute(sql, values)
        connection.commit()
        print(f"Student {first_name} {last_name} added successfully.")
        cursor.close()
        connection.close()

# Retrieve all students from the database
def fetch_students():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        connection.close()

# Example usage
insert_student('John', 'Doe', 20, 'Computer Science')
insert_student('Jane', 'Smith', 22, 'Mathematics')
fetch_students()
