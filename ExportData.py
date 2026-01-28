# Program name: ExportData.py
# Description: Function to export a set of data to a csv file
# Created by: Thierry Perroud
# Last modified by: Thierry Perroud
# Last Modified date: 28.01.2026
# Version : 0.4

# **********************************************************************************************************************
#   Imports
# **********************************************************************************************************************
import sqlite3
import pandas as pd

# **********************************************************************************************************************
#   Functions
# **********************************************************************************************************************

def get_data(id):
    conn = sqlite3.connect('database.db')                                                               # Connection to database
    df = pd.read_sql_query(f"SELECT * FROM Telemetry_measurements WHERE Flight_id = {id}", conn)    # Query for the flight's data
    df.to_csv("DataDump/Flight_Datas.csv", index=False)                                                     # Exporting to csv file

    conn.close()
