from finance_manager import Manager
manager = Manager()

print("\nДобро пожаловать в трекер задач!")
while True:
    print("\n1. Добавить операцию\n"
          "2. Удалить операцию\n"
          "3. Посмотреть операции\n"
          "4. Выйти из программы\n")
    choice_main = int(input("Действие: "))
    print("")
    if choice_main not in (1,2,3,4):
        print("Выберите только числа от 1 до 4!")
    if choice_main == 1:
        print ("1 - Добавить доход\n"
        "2 - Добавить расход\n"
        "3 - Выйти назад в главное меню\n")
        
        choice_1 = int(input("Выбор: "))
        while choice_1 not in (1,2,3):
            print("\nВыберите только числа от 1 до 3!\n")
            print ("1 - Добавить доход\n"
        "2 - Добавить расход\n"
        "3 - Выйти назад в главное меню\n")
            choice_1 = int(input("Выбор: "))
        if choice_1 == 1:
            amount = float(input("Введите сумму: "))
            manager.income(amount)
            print("\nДоход успешно добавлен!")
            
        elif choice_1 == 2:
            amount = float(input("Введите сумму: "))
            manager.expense(amount)
            print("\nРасход успешно добавлен!")
            
        elif choice_1 == 3:
            pass
            
    elif choice_main == 2:
        print('Для возвращения в меню впишите "-1"')
        choice_2 = int(input("Укажите id операции: "))
        if choice_2 != -1:
            manager.delete(choice_2)
            print(f"Задача с id - {choice_2} успешно удалена!")
        else:
            pass
        
    elif choice_main == 3:
        transactions = manager.show()
        print("Список операций: \n")
        for transaction in transactions:
            print (f"id - {transaction[0]} | type - {transaction[1]} | amount - {transaction[2]}")
    elif choice_main == 4:
        print("\nВыход из программы...\n")
        break    