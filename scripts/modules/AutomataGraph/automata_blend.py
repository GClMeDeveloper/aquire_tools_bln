import bpy as b


class Coords:
    def __init__(self):
        self.axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    def gen_cart_graph(self):
        dictionary = {}
        for digit in self.axis:
            for number in self.axis:
                for num in self.axis:
                    dictionary[f"({digit}, {number}, {num})"] = [digit, number, num]
        return dictionary


class Automata(Coords):
    def __init__(self, rules, reach):
        super().__init__()
        self.start_grid = self.gen_cart_graph()
        pass


class Cell(Automata):
    def __init__(self):
        super().__init__(rules=None, reach=None)
        pass

