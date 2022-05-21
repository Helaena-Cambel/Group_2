import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\loren\Downloads\Database1.accdb;')
    print("Connected to a Database")

    Inventors = 'Lorenzo Archibald E. Penaflorida'
    Invention = 'Connecting MS Access Database'
    DateOfInvention = 'May 22, 2022'
    Description = 'We created a table of notable inventors and were able to manipulate it through an external connection with Python. We wrote two codes titled "connects" and "insert" that let us access and input data into the table through Python.'
    user_id = 11

    record = connect.cursor()
    record.execute('UPDATE tblInventor SET Inventors = ? WHERE id=?', (Inventors, user_id))
    record.execute('UPDATE tblInventor SET Invention = ? WHERE id=?', (Invention, user_id))
    record.execute('UPDATE tblInventor SET DateOfInvention = ? WHERE id=?', (DateOfInvention, user_id))
    record.execute('UPDATE tblInventor SET Description = ? WHERE id=?', (Description, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")