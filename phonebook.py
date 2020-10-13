import os
import sqlite3

conn = sqlite3.connect("phonebook_db.sqlite")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS phonebook
                  (name TEXT,
                   number INT)
               """)
conn.commit()


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_all():
    for value in c.execute("SELECT * FROM phonebook"):
        print(value)



def add_user():
    user_name = input('Enter name - ')
    user_phone = input('Enter number - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    if c.fetchone() is None:
        c.execute("INSERT INTO phonebook VALUES (?,?)", (user_name, user_phone))
        conn.commit()
    else:
        print('already EXIST!!')
        # names = [(user_name, user_phone)]
        # c.executemany("INSERT INTO phonebook VALUES (?,?,?)", names)


def change_user():
    user_name = input('Enter name - ')
    # user_phone = input('Enter number - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    if c.fetchone() is None:
        print('NOT Eyi!!')
    else:
        user_phone = input('Введите новый номер - ')
        c.execute(f"UPDATE phonebook SET number = '{user_phone}' WHERE name = '{user_name}'")
        conn.commit()



def del_user():
    pass


def show_user():
    user_name = input('Введите имя - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    if c.fetchone() is None:
        print('Такого имени нет в справочнике.')
    else:
        print(c.fetchone())



def to_choose():
    if choice == 0:
        exit()
    elif choice == 1:
        # screen_cleaner()
        show_all()
        # print('ddd')

    elif choice == 2:
        screen_cleaner()
        add_user()
        pass
    elif choice == 3:
        screen_cleaner()
        change_user()
        pass
    elif choice == 4:
        screen_cleaner()
        del_user()
        pass
    elif choice == 5:
        screen_cleaner()
        show_user()
        pass


while True:
    print("++++++++++++++++++++++++++++++++++\n"
          "+     Телефонный справочник      +\n"
          "++++++++++++++++++++++++++++++++++")

    print("Чего желаете?")
    print("1 - Показать все")
    print("2 - Добавить")
    print("3 - Изменить")
    print("4 - Удалить")
    print("5 - Посмотреть")
    print("0 - Выйти")
    choice = int(input())
    to_choose()
