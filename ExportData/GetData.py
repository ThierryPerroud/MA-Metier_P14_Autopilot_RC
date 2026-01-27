import sqlite3
import pandas as pd

def get_data(id):
    conn = sqlite3.connect('../database.db')                                                               # Connection to database
    df = pd.read_sql_query(f"SELECT * FROM Telemetry_measurements WHERE Flight_id = {id}", conn)    # Query for the flight's data
    df.to_csv("donnees.csv", index=False)                                                     # Exporting to csv file

    conn.close()
