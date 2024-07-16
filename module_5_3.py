# Атрибуты и методы объекта. Домашняя работа по уроку "Перегрузка операторов."

class House:
    # Вунтри класса House определим метод __init__, в который передадим название и кол-во этажей
    def __init__(self, name, number_of_floors):
        self.name = name  # Инициализация атрибута name
        self.number_of_floors = number_of_floors  # Инициализация атрибута number_of_floors

    # Создаем метод go_to с параметром new_floor
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'Такого этажа не существует')

    def __len__(self):  # Возвращает кол-во этажей здания self.number_of_floors
        return self.number_of_floors

    def __str__(self):  # Возвращает строку: "Название: <название>, кол-во этажей: <этажи>"
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):  # Возвращает True, если количество этажей одинаковое у self и у other
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):  # Увеличивает кол-во этажей на переданное значение value, возвращает сам объект self
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors



# Создаем объект класса House с произвольным названием и количеством этажей
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
# print(len(h1))
# print(len(h2))
print(h1 == h2)  # __eq__
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)  # __eq__
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# Вызываем метод go_to у этого объекта с произвольным числом этажей
# h1.go_to(5)
# h2.go_to(10)
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)
