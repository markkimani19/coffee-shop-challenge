class Coffee:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"coffe name = {self.name}"
    
    def coffeName(coffeename):
        if isinstance(coffeename,str) and len(coffeename) >= 3:
            return coffeename
        else:
            raise ValueError("Character Must be a string between 1 to 25")
        
c1= Coffee("White")
print(c1)