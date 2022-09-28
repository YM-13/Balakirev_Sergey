import sys

# программу не менять, только добавить два метода
lst_in = ["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"] #list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        my_dict = {}

        for el in data:
            el_list = el.split(' ')
            for key, value in zip(self.FIELDS, el_list):
                my_dict[key] = value
            self.lst_data.append(my_dict)
            my_dict = {}


    def select(self, a, b):
        """select(self, a, b) - возвращает список из элементов списка (dicts) lst_data в диапазоне [a; b] (включительно)
        по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка."""
        if b < len(self.lst_data):
            ret_list = self.lst_data[a:(b + 1)]
            return ret_list
        else:
            return self.lst_data[a:]


    # здесь добавлять методы


db = DataBase()
db.insert(lst_in)