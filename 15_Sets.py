class CustomSet:
    def __init__(self):
        self.data = set()

    def add(self, value):
        self.data.add(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            print("Value not found")

    def contains(self, value):
        return value in self.data

    def size(self):
        return len(self.data)

    def display(self):
        print(self.data)


s = CustomSet()
s.add(10)
s.add(20)
s.add(20)
s.remove(10)
s.display()
print("Contains 20:", s.contains(20))
print("Size:", s.size())
