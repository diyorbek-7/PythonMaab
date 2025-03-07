import sqlite3
#1
with sqlite3.connect('library.db') as c:
    cursor = c.cursor()
    # cursor.execute('create table library(title text,author text,year_published int,genre text)')

#2
    # data = """
    # insert into library values
    # ('To Kill a Mockingbird','Harper Lee',1960,'Fiction'),
    # ('1984','George Orwell',1949,'Dystopian'),
    # ('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic');
    # """
    # cursor.executescript(data)

#3
    cursor.execute("UPDATE library SET Year_Published = 1950 WHERE Title = '1984'")

#4
    cursor.execute("SELECT Title, Author FROM library WHERE Genre = 'Dystopian'")
    print("Dystopian books:", cursor.fetchall())

# 5. Delete Data
    cursor.execute("DELETE FROM library WHERE Year_Published < 1950")

    cursor.execute("ALTER TABLE library ADD COLUMN Rating REAL")

    cursor.executemany('''
        UPDATE library SET Rating = ? WHERE Title = ?
    ''', [
        (4.8, 'To Kill a Mockingbird'),
        (4.7, '1984'),
        (4.5, 'The Great Gatsby')
    ])
#7
    cursor.execute('select * from library order by year_published asc')
    print(cursor.fetchall())

