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
    
conn = sqlite3.connect('new.db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('information.docx',))
    conn.commit()
conn.close()

conn = sqlite3.connect('new.db')
with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('Hello.txt',))
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('myImage.png',))
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('myMovie.mpg',))
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('World.txt',))
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('data.pdf',))
    cur.execute('INSERT INTO tbl_fileTypes(col_fileType) VALUES (?)', \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()

conn = sqlite3.connect('new.db')
with conn:
    cur = conn.cursor()
    cur.execute('SELECT col_fileType FROM tbl_fileTypes WHERE col_fileType = \
                '?txt'')
    varData = cur.fetchall()
    for item in varData:
        msg = 'Text Documents: ()'.format(item[0])
    print(msg)
