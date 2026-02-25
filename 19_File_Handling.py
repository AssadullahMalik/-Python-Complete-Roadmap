class FileManager:

    def write_file(self, filename, content):
        try:
            with open(filename, "w") as file:
                file.write(content)
            print("File written successfully")
        except Exception as e:
            print("Error while writing:", e)

    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return f"Error: {e}"

    def append_file(self, filename, content):
        try:
            with open(filename, "a") as file:
                file.write(content)
            print("Content appended successfully")
        except Exception as e:
            print("Error while appending:", e)

    def read_lines(self, filename):
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except Exception as e:
            return f"Error: {e}"

 
fm = FileManager()

fm.write_file("sample.txt", "Hello Asadullah\n")
fm.append_file("sample.txt", "Learning Python for AI\n")

print("File Content:")
print(fm.read_file("sample.txt"))

print("File Lines:")
print(fm.read_lines("sample.txt"))

