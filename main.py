import random

choices = {'камень': 1, 'ножницы': 2, 'бумага': 3, 'ящирица': 4, 'спок': 5}
reversed_choices = {v: k for k, v in choices.items()}


def get_user_choice():
    user_input = input("Выберите камень, ножницы, бумага, ящирица, спок: ")

    while user_input.lower() not in choices:
        print("Неверный выбор. Попробуйте еще раз.")
        user_input = input("Выберите камень, ножницы, бумага, ящирица, спок: ")

    return choices[user_input.lower()]


def get_computer_choice():
    pc_input = random.choice(list(choices.keys()))
    return choices[pc_input]


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 1 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 4) or \
            (user_choice == 2 and computer_choice == 3) or \
            (user_choice == 2 and computer_choice == 4) or \
            (user_choice == 3 and computer_choice == 1) or \
            (user_choice == 3 and computer_choice == 5) or \
            (user_choice == 4 and computer_choice == 5) or \
            (user_choice == 4 and computer_choice == 3) or \
            (user_choice == 5 and computer_choice == 1) or \
            (user_choice == 5 and computer_choice == 2):
        print(f"Поздравляю, вы победили! Компьютер выбрал: {reversed_choices[computer_choice]}")
    else:
        print(f"Вы проиграли! Компьютер выбрал: {reversed_choices[computer_choice]}")


while True:
    a = input('вы желаете продолжить?')
    if a.lower() == 'да':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)
    else:
        break
