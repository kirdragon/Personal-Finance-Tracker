from finance_manager import Manager
manager = Manager()

while True:
    print("\n1. Добавить операцию\n"
          "2. Удалить операцию\n"
          "3. Посмотреть операции\n"
          "4. Выйти из программы\n")
    choice_main = int(input("Действие: "))

    if choice_main == 1:
        print ("\n1 - Добавить доход\n"
        "2 - Добавить Расход\n"
        "3 - Выйти назад в главное меню\n")
        
        choice_1 = int(input("Выбор: "))
        while choice_1 not in (1,2,3):
            print("\nВыберите только числа от 1 до 3!\n")
            choice_1 = int(input("Выбор: "))
        if choice_1 == 1:
            amount = float(input("Введите сумму: "))
            manager.income(amount)
            
        elif choice_1 == 2:
            amount = float(input("Введите сумму: "))
            manager.expense(amount)
            
        elif choice_1 == 3:
            pass
            
    elif choice_main == 2:
        choice_2 = int(input("Укажите id операции: "))
        manager.delete(choice_2)
        
    elif choice_main == 3:
        transactions = manager.show()
        for transaction in transactions:
            print (transaction)
    elif choice_main == 4:
        print("\nВыход из программы...\n")
        break    