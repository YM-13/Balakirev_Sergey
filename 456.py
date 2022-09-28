# class Student:
#     name: str = None
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     __repr__ = __str__
#
#
# points = []
# count = 1
# for i in range(1, 1001):
#     if i == 2:
#         points.append(f'p{i} = Point({count}, {count}, "yellow")')
#     else:
#         points.append(f'p{i} = Point({count}, {count})')
#     count += 2
#
# print(points)
# print(len(points))



# def timeit(func):
#     def wrapper():
#         start = datetime.datetime.now()
#         result = func()
#         print(datetime.datetime.now() - start)
#         return result
#     return wrapper

# @timeit
# def one():
#     l = [x for x in range(10**4) if x % 2 == 0]
#     return l
#




# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subject_marks.sort(key = lambda x: x[1])
# print(subject_marks)



x = ['apple', 'banana', 'cherry']
print(id('cherry'))
# print(x[id('banana')])

# x.pop(id('banana'))
# print(x)

print(2 + 2)