import sqlite3

print("<===========Welcomte to Contact Book===========>")

connection=sqlite3.connect("Contact_Book.db")
cursor=connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Contact_Book (Name, Number)")
    connection.commit()

def add_values(name,number):
    values=("INSERT INTO Contact_Book VALUES {}")
    data=(name,number)
    cursor.execute(values.format(data))
    connection.commit()

def delete_table():
    cursor.execute("DROP TABLE Contact_Book")

def delete_values(name):
    command=("DELETE FROM Contact_Book WHERE Name ='{}'")
    cursor.execute(command.format(name))
    connection.commit()
def print_values():
        cursor.execute("SELECT * FROM Contact_Book")
        values=cursor.fetchall()
        for i in values:
            print(i)   

create_table()


while(True):
    try:
        print("""1-Add Value
2-Delete Value
3-Delete Table
4-Show Names and Numbers
5-Exit""")
        answer=int(input("Choose an option: "))
        if answer==1:
            print("\n")
            name=input("Enter name: ")
            number=input("Enter number: ")
            add_values(name,number)
            print("\n")
            continue
        elif answer==2:
            print("\n")
            name=input("Enter name for delete: ")
            delete_values(name)
            print("\n")
            continue
        elif answer==3:
            delete_table()
            print("\n")
            continue
        elif answer==4:
            create_table()
            print("\n<===Values===>")
            print_values()
            print("<============>\n")
            continue
        elif answer==5:
            connection.close()
            break

        else:
            print("\nPlease enter a number between [1-5]")
            print("\n")
            continue   
    except ValueError:
        print("\nPlease enter a number between [1-5]")
        print("\n")
        continue