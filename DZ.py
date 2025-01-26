class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")


store1 = Store("Копеечка", "пр. Ленина 99")
store2 = Store("Техника", "ул. Мира 42")
store3 = Store("Печать", "ул. Победы 18")

store1.add_item("apples", 10.50)
store1.add_item("bananas", 15.75)

store2.add_item("laptop", 45999.99)
store2.add_item("smartphone", 12499.99)

store3.add_item("novel", 115.99)
store3.add_item("magazine", 75.99)

print("\nТестирование магазина Копеечка:")
print(f"Цена на 'apples': {store1.get_price('apples')}")
store1.update_price("apples", 10.55)
print(f"Новая цена на 'apples': {store1.get_price('apples')}")
store1.remove_item("bananas")
print(f"Цена на 'bananas' после удаления: {store1.get_price('bananas')}")