import psycopg2
import csv
import config

def connect_to_db():
    try:
        conn = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password, host=config.host)
        print("Connection established successfully.")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def insert_values(dbname, username, phone, conn):
    try:
        cursor = conn.cursor()

        command = f"""
            INSERT INTO {dbname} (username, phone)
            VALUES (%s,%s);
        """
        #avoiding sql injection
        cursor.execute(command, (username, phone))
        
        conn.commit()
        print("Data inserted successfully.")

    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def create_table(name):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        command = f"""
            CREATE TABLE IF NOT EXISTS "{name}" (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                phone VARCHAR(11) UNIQUE NOT NULL
            )
        """

        cursor.execute(command)
        conn.commit()
        print("Table created successfully.")

    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()

def upload_from_csv(dbname, csv_file):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                username, phone = row
                insert_values(dbname, username, phone, conn)

        print("Data uploaded from CSV successfully.")

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()

def update_data(dbname, username, new_username=None, new_phone=None):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        if new_username:
            cursor.execute(f"UPDATE {dbname} SET username = %s WHERE username = %s", (new_username, username))
        if new_phone:
            cursor.execute(f"UPDATE {dbname} SET phone = %s WHERE username = %s", (new_phone, username))

        conn.commit()
        print("Data updated successfully.")

    except psycopg2.Error as e:
        print(f"Error updating data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()

def query_data(dbname, filter_column=None, filter_value=None):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        if filter_column and filter_value:
            cursor.execute(f"SELECT * FROM {dbname} WHERE {filter_column} = %s", (filter_value,))
        else:
            cursor.execute(f"SELECT * FROM {dbname}")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except psycopg2.Error as e:
        print(f"Error querying data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()

def delete_data(dbname, username=None, phone=None):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        if username:
            cursor.execute(f"DELETE FROM {dbname} WHERE username = %s", (username,))
        elif phone:
            cursor.execute(f"DELETE FROM {dbname} WHERE phone = %s", (phone,))
        else:
            print("Please specify either username or phone for deletion.")

        conn.commit()
        print("Data deleted successfully.")

    except psycopg2.Error as e:
        print(f"Error deleting data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    name = input("Enter table name: ")
    action = input("Choose action (1: Upload from CSV, 2: Enter data manually, 3: Update data, 4: Query data, 5: Delete data): ")

    if action == "1":
        csv_file = input("Enter CSV file path: ")
        upload_from_csv(name, csv_file)
    elif action == "2":
        username = input("Enter username: ")
        phone = input("Enter phone number: ")
        insert_values(name, username, phone, connect_to_db())
    elif action == "3":
        username = input("Enter username to update: ")
        new_username = input("Enter new username (leave blank to keep unchanged): ")
        new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
        update_data(name, username, new_username, new_phone)
    elif action == "4":
        filter_column = input("Enter column to filter by (leave blank to retrieve all data): ")
        filter_value = input("Enter value to filter by (leave blank to retrieve all data): ")
        query_data(name, filter_column, filter_value)
    elif action == "5":
        username = input("Enter username to delete (leave blank if deleting by phone): ")
        phone = input("Enter phone number to delete (leave blank if deleting by username): ")
        delete_data(name, username, phone)
    else:
        print("Invalid action.")
