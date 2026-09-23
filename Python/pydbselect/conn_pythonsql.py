import os
import mssql_python
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read connection settings
CONNSTRING = os.getenv("SOURCE_CONNECTION_STRING")

#TABLE_NAME = "fdap.V_ABB_DB1_1Hour"
TABLE_NAME = "config.V_Tag"

try:
    # Create connection

    # ── Download from source ──
    with mssql_python.connect(CONNSTRING) as conn:
        cursor = conn.cursor()

    # Query top 10 rows
        query = f"SELECT TOP 10 * FROM {TABLE_NAME}"
        cursor.execute(query)

    # Fetch rows
        rows = cursor.fetchall()

    # Print results
        for row in rows:
            print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        cursor.close()
        conn.close()
    except Exception:
        pass