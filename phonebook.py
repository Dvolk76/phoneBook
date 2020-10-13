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
    user_name = input('Введите имя - ')
    user_phone = input('Введите номер - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    if c.fetchone() is None:
        c.execute("INSERT INTO phonebook VALUES (?,?)", (user_name, user_phone))
        conn.commit()
    else:
        print('Такое имя уже существует!')


def change_user():
    user_name = input('Введите имя - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    if c.fetchone() is None:
        print('Такого имени нет в справочнике!')
    else:
        user_phone = input('Введите новый номер - ')
        c.execute(f"UPDATE phonebook SET number = '{user_phone}' WHERE name = '{user_name}'")
        conn.commit()


def del_user():
    user_name = input('Введите имя - ')
    c.execute(f"DELETE FROM phonebook WHERE name = '{user_name}'")
    conn.commit()
    print('УДАЛЕН!')


def show_user():
    user_name = input('Введите имя - ')
    c.execute(f"SELECT name FROM phonebook WHERE name = '{user_name}'")
    the_user = c.fetchone()
    if the_user is None:
        print('Такого имени нет в справочнике!')
    else:
        c.execute(f"SELECT name, number FROM phonebook WHERE name = '{user_name}'")
        the_user = c.fetchone()
        print(the_user)


def to_choose():
    if choice == 0:
        exit()
    elif choice == 1:
        show_all()

    elif choice == 2:
        screen_cleaner()
        add_user()

    elif choice == 3:
        screen_cleaner()
        change_user()

    elif choice == 4:
        screen_cleaner()
        del_user()

    elif choice == 5:
        screen_cleaner()
        show_user()


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
