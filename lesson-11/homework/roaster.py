import sqlite3


#1
# with sqlite3.connect('roaster.db') as c:
#     query = 'create table roaster (name text,species text,age int)'
#     cursor = c.cursor()
#     data = cursor.execute(query)

#2
# name = input('name:')
# species = input('species:')
# age = input('age:')
# query = f"insert into roaster values ('{name}','{species}','{age}')"
# with sqlite3.connect('roaster.db') as c:
#     cursor = c.cursor()
#     data = cursor.executescript(query)

#3
# query = "UPDATE roaster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'"
with sqlite3.connect('roaster.db') as c:
    cursor = c.cursor()
#     cursor.execute(query)

#4
    cursor.execute("SELECT Name, Age FROM roaster WHERE Species = 'Bajoran'")
    print("Bajoran characters:", cursor.fetchall())

#5
    cursor.execute('delete from roaster where age>100')
    c.commit()

#7
    cursor.executemany('''
        UPDATE Roster SET Rank = ? WHERE Name = ?
    ''', [
        ('Captain', 'Benjamin Sisko'),
        ('Lieutenant', 'Ezri Dax'),
        ('Major', 'Kira Nerys')
    ])
#8
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("Roster sorted by Age:", cursor.fetchall())

