#Importing the library for database..
import sqlite3
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Predictions (
                 Name TEXT,
                 Symptom1 TEXT,
                 Symptom2 TEXT,
                 Symptom3 TEXT,
                 Symptom4 TEXT,
                 Symptom5 TEXT,
                 Disease TEXT)""")
    conn.commit()
    conn.close()
#Method to save the result in the database..
def save_prediction(name, symptoms, disease):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Predictions (Name, Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, Disease) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, *symptoms, disease))
    conn.commit()
    conn.close()

#Initialize database
init_db()
