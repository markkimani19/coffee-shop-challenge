class Customer:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"customer name = {self.name}"

    
    def customerName(name):

        if isinstance(name,str) and 1 <= len(name) <= 15:
            return name
        else:
            raise ValueError("Character Must be a string between 1 to 25")
        
customer = Customer("Mark")
print(customer)


    

    

    
    

