import json


class Stock:
    def __init__(self, stock_id, name, quantity, price):
        self.stock_id = stock_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "stock_id": self.stock_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


class StockManager:
    def __init__(self, filename="stocks.json"):
        self.filename = filename
        self.stocks = self.load_stocks()  # List of dictionaries

    def load_stocks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)  # List of dictionaries
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_stocks(self):
        with open(self.filename, "w") as file:
            json.dump(self.stocks, file, indent=4)

    def add_stock(self, stock_id, name, quantity, price):
        for stock in self.stocks:
            if stock["stock_id"] == stock_id:
                print("Stock with this ID already exists.")
                return

        new_stock = Stock(stock_id, name, quantity, price)
        self.stocks.append(new_stock.to_dict())  # List append (dict)
        self.save_stocks()
        print("Stock added successfully.")

    def view_stocks(self):
        if not self.stocks:
            print("No stocks found.")
            return

        for stock in self.stocks:  # Iterating list of dicts
            print("-------------------------")
            print("Stock ID:", stock["stock_id"])
            print("Name:", stock["name"])
            print("Quantity:", stock["quantity"])
            print("Price:", stock["price"])

    def search_stock(self, stock_id):
        for stock in self.stocks:
            if stock["stock_id"] == stock_id:
                print("Stock Found:")
                print(stock)
                return
        print("Stock not found.")

    def delete_stock(self, stock_id):
        for stock in self.stocks:
            if stock["stock_id"] == stock_id:
                self.stocks.remove(stock)
                self.save_stocks()
                print("Stock deleted successfully.")
                return
        print("Stock not found.")

    def update_stock(self, stock_id, quantity=None, price=None):
        for stock in self.stocks:
            if stock["stock_id"] == stock_id:
                if quantity is not None:
                    stock["quantity"] = quantity
                if price is not None:
                    stock["price"] = price

                self.save_stocks()
                print("Stock updated successfully.")
                return
        print("Stock not found.")


def main():
    manager = StockManager()

    # Tuple for menu options (immutable)
    menu_options = (
        "1. Add Stock",
        "2. View Stocks",
        "3. Search Stock",
        "4. Delete Stock",
        "5. Update Stock",
        "6. Exit"
    )

    while True:
        print("\nStock Management System")
        for option in menu_options:
            print(option)

        choice = input("Enter choice: ")

        if choice == "1":
            stock_id = input("Enter Stock ID: ")
            name = input("Enter Stock Name: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")

            try:
                quantity = int(quantity)
                price = float(price)
                manager.add_stock(stock_id, name, quantity, price)
            except ValueError:
                print("Quantity must be integer and price must be number.")

        elif choice == "2":
            manager.view_stocks()

        elif choice == "3":
            stock_id = input("Enter Stock ID to search: ")
            manager.search_stock(stock_id)

        elif choice == "4":
            stock_id = input("Enter Stock ID to delete: ")
            manager.delete_stock(stock_id)

        elif choice == "5":
            stock_id = input("Enter Stock ID to update: ")
            quantity = input("Enter new quantity (or press enter to skip): ")
            price = input("Enter new price (or press enter to skip): ")

            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            manager.update_stock(stock_id, quantity, price)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
    
