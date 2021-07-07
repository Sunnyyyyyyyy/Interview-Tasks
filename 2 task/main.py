import re


class User:
    # Стартові значення
    level = 0
    experience = 0
    actions_left = 3

    # Створення користувача
    def __init__(self, username, is_paid=False, paid_days=0):
        # Пусте ім'я
        if len(username) == 0:
            raise Exception("Username is empty")
        # Є заборонені символи
        if len(re.findall(r'[a-zA-Z0-9\-\.\_]', username)) < len(username):
            raise Exception("Username has restricted symbol")
        # Все добре
        self.username = username
        self.is_paid = is_paid
        self.paid_days = paid_days

    # Дія
    def action(self, experience):
        # Платний користувач
        if self.is_paid:
            self.experience += experience
        # Безкоштовний, але ще є дії
        elif self.actions_left > 0:
            self.experience += experience
            self.actions_left -= 1
        # Безкоштовний і уже немає дій
        else:
            print("You have used all actions")

    # Метод щоночі
    def midnight(self):
        # Перерахунок досвіду і рівню
        self.level += self.experience // 500
        self.experience %= 500

        # Зменшення кількості днів для платних
        if self.is_paid:
            self.paid_days -= 1
            if self.paid_days == 0:
                self.is_paid = False

        # Збільшення кількості дій для безкоштовних (при необхідності)
        if self.actions_left < 3:
            self.actions_left = 3

    # Для зручного виводу
    def __str__(self):
        return f'''Username: {self.username}
Level: {self.level}
Experience: {self.experience}
Actions left: {self.actions_left}
Paid: {self.is_paid}
Paid days left: {self.paid_days}
'''


# Псевдодебаг
test = User("Test")
test.action(100)
test.action(1000)
print(test)
print("\n"*5)
test.midnight()
print(test)