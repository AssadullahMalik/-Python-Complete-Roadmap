class CustomDictionary:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print("Key not found")

    def get(self, key):
        return self.data.get(key, "Key not found")

    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def size(self):
        return len(self.data)

    def display(self):
        print(self.data)


d = CustomDictionary()
d.add("name", "Asadullah")
d.add("age", 21)
d.add("marks", 95)

d.display()
print("Name:", d.get("name"))
print("Keys:", d.keys())
print("Size:", d.size())
