class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name}: нет в наличии, невозможно удалить.")

    def get_price(self, item_name):
        if item_name in self.items:
            return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"{item_name} нет в наличии2")

    def display(self):
        print(f"Товары в магазине {self.name}:")
        for item, price in self.items.items():
            print(f"{item}: {price} руб.")

store1 = Store("Пятерочка", "ул.Арбат")
store1.add_item("яблоки", 100)
store1.add_item("груши", 150)
store1.add_item("колбаса", 500)
store1.display()

store2 = Store("Дикси", "Рязанский проспект")
store2.add_item("сыр", 800)
store2.add_item("ветчина", 1000)
store2.add_item("колбаса", 600)
store2.display()

store3 = Store("Вкусвилл", "Проспект Мира")
store3.add_item("молоко", 88)
store3.add_item("хлеб", 75)
store3.add_item("орехи", 900)
store3.display()

store1.remove_item("яблоки")
store1.remove_item("икра")
store1.update_price("груши", 200)
print("После изменений:")
store1.display()
