class Tutorial:
    title = "Атрибут класса"

    def __init__(self, name):
        self.name = name  # локальный атрибут (локальное свойство)

t = Tutorial("lesson")
print(t.__dict__)  # Вывод локальных свойств объекта/экземпляра класса
print(Tutorial.__dict__) # Вывод атрибутов класса