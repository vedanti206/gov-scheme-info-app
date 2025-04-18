import sqlite3
import os

# Check the current directory
print(f"Current working directory: {os.getcwd()}")

def init_db():
    # Use absolute path for the database file to ensure it's being created in the correct location
    db_path = os.path.join(os.getcwd(), 'schemes.db')  # This ensures it uses the current working directory
    print(f"Initializing database at {db_path}")
    
    # Create or connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create table if it doesn't exist
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

def insert_sample_data():
    db_path = os.path.join(os.getcwd(), 'schemes.db')
    print(f"Inserting data into database at {db_path}")
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Sample data
    schemes = [
        ("Scheme 1", "This is the description of Scheme 1. It helps people with certain needs.", "Eligibility Criteria 1: Age 18-40", "Document1.pdf, Document2.pdf", "Step 1: Apply, Step 2: Verification", "http://scheme1.com", "Helpline 1: 1800-000-0001"),
        ("Scheme 2", "This is the description of Scheme 2. It supports students in need of financial aid.", "Eligibility Criteria 2: Students enrolled in recognized institutions", "Document3.pdf, Document4.pdf", "Step 1: Register, Step 2: Submit Documents", "http://scheme2.com", "Helpline 2: 1800-000-0002"),
        ("Scheme 3", "Description of Scheme 3: Supports farmers with subsidies for seeds.", "Eligibility Criteria 3: Farmers with land", "Document5.pdf, Document6.pdf", "Step 1: Apply, Step 2: Submit Land Proof", "http://scheme3.com", "Helpline 3: 1800-000-0003"),
        ("Scheme 4", "Description of Scheme 4: Provides healthcare support to low-income families.", "Eligibility Criteria 4: Low-income families", "Document7.pdf, Document8.pdf", "Step 1: Visit Clinic, Step 2: Register", "http://scheme4.com", "Helpline 4: 1800-000-0004")
    ]

    c.executemany(''' 
        INSERT INTO schemes (name, description, eligibility, documents, application_steps, official_link, helpline)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', schemes)

    conn.commit()
    conn.close()

# First, initialize the database and create the table
init_db()

# Then, insert sample data
insert_sample_data()
