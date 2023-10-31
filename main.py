from flask import Flask
import psycopg2
import util

app = Flask(__name__)

# PostgreSQL connection settings
db_settings = {
    'dbname': 'postgres',
    'user': 'raywu1990',
    'password': 'test',
    'host': '127.0.0.1',
    'port': '5432',
}

def connect_to_db():
    try:
        conn = psycopg2.connect(**db_settings)
        cursor = conn.cursor()
        return cursor, conn
    except psycopg2.Error as e:
        raise e

def disconnect_from_db(cursor, conn):
    try:
        cursor.close()
        conn.close()
    except Exception as e:
        raise e

@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        cursor, connection = connect_to_db()

        # Insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        connection.commit()

        return "Success!"
    except psycopg2.Error as e:
        error_message = str(e)
        return f"Error: {error_message}"
    finally:
        disconnect_from_db(cursor, connection)

@app.route('/api/unique')
def unique_fruits():
    try:
        cursor, conn = connect_to_db()

        # Fetch unique fruits from basket_a and basket_b
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a UNION SELECT DISTINCT fruit_b FROM basket_b;")
        result = cursor.fetchall()

        # Create an HTML table to display the unique fruits
        table_html = "<table>"
        for row in result:
            table_html += f"<tr><td>{row[0]}</td></tr>"
        table_html += "</table>"

        return table_html
    except psycopg2.Error as e:
        error_message = str(e)
        return f"Error: {error_message}"
    finally:
        disconnect_from_db(cursor, conn)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
