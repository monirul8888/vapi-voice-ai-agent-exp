from database import engine, init_db
from sqlalchemy import text

# Ensure tables exist
init_db()

def run_sql(query: str):
    """Run a raw SQL query and return results or affected row count."""
    with engine.begin() as conn:
        result = conn.execute(text(query))
        # Return fetched rows for SELECT, rowcount for INSERT/UPDATE/DELETE
        return result.fetchall() if result.returns_rows else result.rowcount

# --- INSERT example ---
insert_query = """
INSERT INTO appointments (patient_name, reason, start_time, canceled, created_at)
VALUES ('John Doe', 'Checkup', '2026-01-24 14:30:00', 0, '2026-01-01 12:00:00')
"""
rows_inserted = run_sql(insert_query)
print("Rows inserted:", rows_inserted)

# --- SELECT example ---
select_query = "SELECT * FROM appointments"
rows = run_sql(select_query)
print("Rows in DB:", rows)