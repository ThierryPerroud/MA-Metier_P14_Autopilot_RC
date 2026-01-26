import sqlite3

# connexion à la base
conn = sqlite3.connect('../database.db')
cur = conn.cursor()

cur.execute("SELECT Latitude, Longitude FROM telemetry_measurements")
resultPosition= [list(row) for row in cur.fetchall()]

print(resultPosition)

cur.execute("SELECT Altitude FROM telemetry_measurements")
resultAltitude = [[row[0], i*10] for i, row in enumerate(cur.fetchall())]

print(resultAltitude)

conn.close()