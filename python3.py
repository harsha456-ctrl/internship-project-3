import sqlite3

def setup_db():
    conn = sqlite3.connect(":memory:")  # In-memory database for temporary storage
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date TEXT, 
            category TEXT, 
            amount REAL, 
            description TEXT
        )
    """)
    conn.commit()
    return conn, c

def add_expense(conn, c, date, category, amount, description):
    try:
        c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                  (date, category, amount, description))
        conn.commit()
    except ValueError:
        pass  # Handle invalid input if needed

def view_expenses(c):
    c.execute("SELECT * FROM expenses")
    return c.fetchall()

# Example usage
if __name__ == "__main__":
    conn, c = setup_db()
    add_expense(conn, c, "2024-02-24", "Food", 12.5, "Lunch")
    add_expense(conn, c, "2024-02-25", "Transport", 5.0, "Bus fare")
    print(view_expenses(c))  # Output stored expenses
    conn.close()
