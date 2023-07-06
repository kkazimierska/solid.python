class IShape:
    def draw_square(self):
        raise NotImplementedError

class Square(IShape):
    pass

s = Square()
s.draw_square()