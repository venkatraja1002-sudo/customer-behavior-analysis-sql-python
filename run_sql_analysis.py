import os
import urllib.parse
from sqlalchemy import create_engine, text

USERNAME = "root"
PASSWORD = urllib.parse.quote_plus("Venkat@123")
HOST = "localhost"
DB_NAME = "shopeasy"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQL_FILE = os.path.join(BASE_DIR, "sql", "analysis.sql")

engine = create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"
)

with open(SQL_FILE, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Split by semicolon safely (simple approach)
statements = [s.strip() for s in sql_script.split(";") if s.strip()]

print("📌 Running SQL analysis...\n")

with engine.connect() as conn:
    for stmt in statements:
        # show each query header
        print("▶", stmt.split("\n")[0][:80], "...\n")
        try:
            result = conn.execute(text(stmt))
            if result.returns_rows:
                rows = result.fetchall()
                cols = result.keys()
                # print table-like output
                print("Columns:", list(cols))
                for r in rows[:20]:
                    print(r)
                if len(rows) > 20:
                    print(f"... ({len(rows)} rows total, showing 20)\n")
                else:
                    print()
            else:
                print("✅ Done\n")
        except Exception as e:
            print("❌ Error running statement:\n", stmt, "\nReason:", e, "\n")

print("✅ SQL analysis finished.")