import os
import pyodbc
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read connection settings
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


# Connect to SQL Server
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# Execute query local test & kloak
#SELECT TOP 10 *
#FROM FDAP.fdap.V_RAO_HourData
#""")

# Heating
#SELECT TOP 10 *
#FROM FDAP.eam.V_ABB_DB1_COUNTERS  
#""")


cursor.execute("""
SELECT TOP 10 *
FROM FDAP.fdap.V_RAO_HourData
""")

# Print results
columns = [column[0] for column in cursor.description]

for row in cursor.fetchall():
    print(dict(zip(columns, row)))

cursor.close()
conn.close()