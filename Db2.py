import sqlite3

conn = sqlite3.connect('new.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_fileTypes( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileType TEXT \
        )')
    conn.commit()
conn.close()
    
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('information.docx'))
    conn.commit()
conn.close()
