import os


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
    choice = input('-')
    to_choose()

    def screen_cleaner(flag):
        if flag:
            os.system('cls' if os.name == 'nt' else 'clear')


    def to_choose():
        if choice == 0:
            exit()
        elif choice == 1:
            screen_cleaner()
            show_all()

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


    def show_all():
        pass


    def add_user():
        pass


    def change_user():
        pass


    def del_user():
        pass


    def show_user():
        pass












