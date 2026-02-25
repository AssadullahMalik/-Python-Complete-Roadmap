class CustomList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            print("Value not found")

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return "Index out of range"

    def size(self):
        return len(self.data)

    def display(self):
        print(self.data)


lst = CustomList()
lst.add(10)
lst.add(20)
lst.add(30)
lst.remove(20)
lst.display()
print("Element at index 1:", lst.get(1))
print("Size:", lst.size())
