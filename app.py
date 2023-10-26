# Import necessary libraries
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
# PostgreSQL database connection information
db_params = {
    "host": "127.0.0.1",
    "database": "dvdrental",
    "user": "raywu1990",
    "password": "test"
}

# Route to insert a new row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        conn.commit()

        # Close the database connection
        conn.close()

        return "Success!"
    except Exception as e:
        return str(e)

# Route to show unique fruits from both baskets
@app.route('/api/unique')
def unique_fruits():
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Get unique fruits from basket_a and basket_b
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a;")
        unique_fruits_a = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b;")
        unique_fruits_b = [row[0] for row in cursor.fetchall()]

        # Close the database connection
        conn.close()

        # Render an HTML table to display unique fruits
        return render_template('unique_fruits.html', fruits_a=unique_fruits_a, fruits_b=unique_fruits_b)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

