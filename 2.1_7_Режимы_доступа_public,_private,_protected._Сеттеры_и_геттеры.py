class Line:

    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)


    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


gg = Line(3, 5, 44, 77)
gg.draw()
gg.set_coords(3, 4, 5 , 6)
gg.draw()