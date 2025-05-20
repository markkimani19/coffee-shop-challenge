class Customer:
    all = []


    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    def __repr__(self):
        return f"customer name = {self.name}"


    @property
    def name(self):
        return self._name

    @name.setter

    def customerName(name):

        if isinstance(name,str) and 1 <= len(name) <= 15:
            return name
        else:
            raise ValueError("Character Must be a string between 1 to 25")


    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
        
# customer = Customer("Mark")
# print(customer)


    

    

    
    

