class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        if not isinstance(customer, customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
@property
def customer(self):
    return self._customer
@property
def coffee(self):
    return self._coffee
@property
def price(self):
    return self._price



