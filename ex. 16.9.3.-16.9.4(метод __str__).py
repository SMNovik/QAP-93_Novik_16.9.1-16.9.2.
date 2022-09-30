# 16.9.3.-16.9.4


class Client:
    def __init__(self, name, surname, city, total):
        self.name = name
        self.surname = surname
        self.city = city
        self.total = total

    def __str__(self):
        return f"{self.name}.{self.surname}.{self.city}.Баланс: {self.total}"

    def info(self):
        return f"{self.name}.{self.surname}.г.{self.city}."


cl1 = Client('Вася', 'Петров', 'Москва', 50)
cl2 = Client('Петя', 'Сидоров', 'Елец', 50)
cl3 = Client('Эмма', 'Яшина', 'Истра', 50)

clients = [cl1, cl2, cl3]

for cl in clients:
    print(cl.info())