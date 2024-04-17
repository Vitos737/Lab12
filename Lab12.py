class Entity:
  _id_counter = 1

  def __init__(self):
      self._id = Entity._id_counter
      Entity._id_counter += 1

  def get_id(self):
      return self._id


class Buyer(Entity):
  def __init__(self, name, address, balance):
      super().__init__()
      self._name = name
      self._address = address
      self._balance = balance

  def get_name(self):
      return self._name

  def set_name(self, name):
      self._name = name

  def get_address(self):
      return self._address

  def set_address(self, address):
      self._address = address

  def get_balance(self):
      return self._balance

  def set_balance(self, balance):
      self._balance = balance

  def __str__(self):
      return f"Buyer ID: {self.get_id()}, Name: {self._name}, Address: {self._address}, Balance: {self._balance}"


class Seller(Entity):
  def __init__(self, name, products=None):
      super().__init__()
      self._name = name
      self._products = products if products else []

  def get_name(self):
      return self._name

  def set_name(self, name):
      self._name = name

  def get_products(self):
      return self._products

  def add_product(self, product):
      self._products.append(product)

  def remove_product(self, product):
      self._products.remove(product)

  def __str__(self):
      return f"Seller ID: {self.get_id()}, Name: {self._name}, Products: {self._products}"


class Order(Entity):
  def __init__(self, buyer, seller, product, delivery_address):
      super().__init__()
      self._buyer = buyer
      self._seller = seller
      self._product = product
      self._delivery_address = delivery_address

  def get_buyer(self):
      return self._buyer

  def get_seller(self):
      return self._seller

  def get_product(self):
      return self._product

  def get_delivery_address(self):
      return self._delivery_address

  def __str__(self):
      return f"Order ID: {self.get_id()}, Buyer: {self._buyer.get_name()}, Seller: {self._seller.get_name()}, Product: {self._product}, Delivery Address: {self._delivery_address}"


class Product:
  def __init__(self, name, price):
      self._name = name
      self._price = price

  def get_name(self):
      return self._name

  def set_name(self, name):
      self._name = name

  def get_price(self):
      return self._price

  def set_price(self, price):
      self._price = price

  def __str__(self):
      return f"Product Name: {self._name}, Price: {self._price}"


# Створення товарів
product1 = Product("Лаптоп", 1200)
product2 = Product("Смартфон", 800)
product3 = Product("Планшет", 500)

# Створення продавців
seller1 = Seller("Best Electronics")
seller1.add_product(product1)
seller1.add_product(product2)

seller2 = Seller("Gadget World")
seller2.add_product(product2)
seller2.add_product(product3)

# Створення покупців
buyer1 = Buyer("John Doe", "123 Main St", 2000)
buyer2 = Buyer("Jane Smith", "456 Elm St", 1500)

# Оформлення замовлень
order1 = Order(buyer1, seller1, product1.get_name(), buyer1.get_address())
order2 = Order(buyer2, seller2, product2.get_name(), buyer2.get_address())

# Вивід інформації про замовлення
print(order1)
print(order2)

# Перевірка балансу після замовлення
print(f"Баланс покупця {buyer1.get_name()}: ${buyer1.get_balance()}")
print(f"Баланс покупця {buyer2.get_name()}: ${buyer2.get_balance()}")