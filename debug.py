from customer import Customer
from coffee import Coffee
from order import Order

mark = Customer("Mark")
titus = Customer("Titus")

edward = Coffee("Edward")
asenath = Coffee("Asenath")

mark.create_order(edward, 3.5)
mark.create_order(asenath, 4.0)
titus.create_order(edward, 5.5)

print("Mark's coffees:", mark.coffees())
print("Latte orders:", edward.orders())
print("Latte average price:", edward.average_price())
