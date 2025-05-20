class Coffee:


    all = []


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"coffe name = {self.name}"
    
    def coffeName(coffeename):
        if isinstance(coffeename,str) and len(coffeename) >= 3:
            return coffeename
        else:
            raise ValueError("Character Must be a string between 1 to 25")


    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0
        
# c1= Coffee("White")
# print(c1)


@classmethod
def most_aficionado(cls, coffee):
    customer_spend = {}


    for order in Order.all:


        if order.coffee == coffee:
            customer_spend[order.customer] = customer_spend.get(order.customer, 0) + order.price



    if not customer_spend:
        return None

    return max(customer_spend, key=customer_spend.get)
