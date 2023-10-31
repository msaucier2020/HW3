from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# PostgreSQL connection settings
db_settings = {
    'dbname': 'dvdrental',
    'user': 'raywu1990',
    'password': 'test',
    'host': '127.0.0.1',
    'port': '5432'
}

@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        conn = psycopg2.connect(**db_settings)
        cursor = conn.cursor()

        # Insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        conn.commit()

        return "Success!"
    except psycopg2.Error as e:
        error_message = str(e)
        return f"Error: {error_message}"
    finally:
        cursor.close()
        conn.close()

@app.route('/api/unique')
def unique_fruits():
    try:
        conn = psycopg2.connect(**db_settings)
        cursor = conn.cursor()

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
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
