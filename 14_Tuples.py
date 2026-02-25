class TupleOperations:
    def __init__(self, data):
        self.data = tuple(data)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return "Index out of range"

    def count(self, value):
        return self.data.count(value)

    def length(self):
        return len(self.data)

    def display(self):
        print(self.data)


t = TupleOperations([10, 20, 30, 20])
t.display()
print("Element at index 1:", t.get(1))
print("Count of 20:", t.count(20))
print("Length:", t.length())
