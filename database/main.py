import sqlite3
conn = sqlite3.connect('database/college.sqlite3')
mycr = conn.cursor()

mycr.execute("""
CREATE TABLE IF NOT EXISTS students(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      address TEXT NOT NULL)

""")

def insert():
    mycr.execute("""
    INSERT INTO students(name,email,address) 
                VALUES('sita','sita@gmail.com','kathmandu')
                """)

    conn.commit()


def select():
    mycr.execute("SELECT * FROM students")
    result = mycr.fetchall()
    # result = mycr.fetchone()
    # result = mycr.fetchmany(1)
    print(result)

select()
    
def delete():
    mycr.execute("DELETE FROM students WHERE id=2")
    conn.commit()
   

# delete()
    
def update():
    mycr.execute("UPDATE students SET name='ram' WHERE id=2")
    conn.commit()

update()