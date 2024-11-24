
class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subcategories = []
    
    def add_subcategory(self, category):
        self.subcategories.append(category)
    
    def display(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}{self.name}")
        for subcategory in self.subcategories:
            subcategory.display(level + 1)


electronics = Category("Elektronik")

phones = Category("Telefonlar", electronics)
laptops = Category("Bilgisayarlar", electronics)

electronics.add_subcategory(phones)
electronics.add_subcategory(laptops)

smartphones = Category("Akıllı Telefonlar", phones)
old_phones = Category("Eski Model Telefonlar", phones)

phones.add_subcategory(smartphones)
phones.add_subcategory(old_phones)

electronics.display()
