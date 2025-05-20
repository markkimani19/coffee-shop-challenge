import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_customer_name(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 20)  # Too long

    def test_create_order(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = customer.create_order(coffee, 4.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)

if __name__ == "__main__":
    unittest.main()
