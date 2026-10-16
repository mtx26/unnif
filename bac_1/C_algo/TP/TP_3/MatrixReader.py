class MatrixReader:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        return MatrixReaderIterator(self.path)

    def get_not_null(self):
        n = 0

        for position, value in self:
            if value != 0:
                n += 1

        return n

    def get_position(self, x, y):
        for position, value, char_position in self:
            if position == (x, y):
                return char_position


class MatrixReaderIterator:

    def __init__(self, path):
        self.file = open(path, "r")
        self.n = 0
        self.row = 0
        self.col = 0

    def __iter__(self):
        return self

    def __next__(self):
        char_position = self.n

        content = self.file.read(3)

        if content == "" or len(content) < 3:
            self.file.close()
            raise StopIteration

        position = (self.row, self.col)
        number = int(content)

        separator = self.file.read(1)

        self.n += len(content) + len(separator)

        if separator == " ":
            self.col += 1
        elif separator == "\n":
            self.row += 1
            self.col = 0

        return position, number, char_position

m = MatrixReader("bac_1/C_algo/TP/TP_3/map_small.txt")
print(m.get_position(2, 4))
with open("bac_1/C_algo/TP/TP_3/map_small.txt", "r") as f:
    f.seek(m.get_position(2, 4))
    print(f.read(3))

for i in m:
    print(i)
