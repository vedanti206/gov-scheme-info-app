from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

DATABASE = 'schemes.db'

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS schemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            eligibility TEXT,
            documents TEXT,
            application_steps TEXT,
            official_link TEXT,
            helpline TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

# ----------------------------
# Routes
# ----------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schemes')
def schemes():
    conn = get_db_connection()
    schemes = conn.execute("SELECT * FROM schemes").fetchall()
    conn.close()
    return render_template('schemes.html', schemes=schemes)

@app.route('/details/<int:scheme_id>')
def details(scheme_id):
    conn = get_db_connection()
    scheme = conn.execute("SELECT * FROM schemes WHERE id=?", (scheme_id,)).fetchone()
    conn.close()

    if scheme is None:
        return render_template('404.html'), 404

    return render_template('details.html', scheme=scheme)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        eligibility = request.form['eligibility']
        documents = request.form['documents']
        application_steps = request.form['application_steps']
        official_link = request.form['official_link']
        helpline = request.form['helpline']

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO schemes 
            (name, description, eligibility, documents, application_steps, official_link, helpline)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, description, eligibility, documents, application_steps, official_link, helpline))
        conn.commit()
        conn.close()

        flash('Scheme added successfully!', 'success')
        return redirect(url_for('schemes'))

    return render_template('add_scheme.html')


# ----------------------------
# Run Flask App
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
