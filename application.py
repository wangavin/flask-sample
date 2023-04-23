from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Connect to the database
    conn = psycopg2.connect(database="tornadoes_db",
                            user="postgres",
                            password="project3",
                            host="database-2.cjrkxejkebqc.us-east-1.rds.amazonaws.com", port="5432")

    # create a cursor
    cur = conn.cursor()

    # Select all products from the table
    cur.execute('''SELECT yr, mo, st, mag, inj, fat, slat, slon, len, wid FROM tornadoes_project''')

    # Fetch the data
    data = cur.fetchall()

    # close the cursor and connection
    cur.close()
    conn.close()

    # return the data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
