class Packages:
    def __init__(self, name, weight, price, type, content=None, category=None, dimension=None, order_status=None, address = None, domiciliary = None):
        self.__name = name
        self.__weight = f"{weight} kg"
        self.__price = price
        self.__type = type
        self.__content = content if content else []
        self.__category = category if category else []
        self.__dimension = dimension if dimension else []
        self.__order_status = order_status
        self.__address = address
        self.__domiciliary = domiciliary       
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @property
    def weight(self):
        return self.__weight    
    @weight.setter
    def weight(self, new_weight):
        self.__weight = f"{new_weight} kg"
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,new_type):
        self.__type = new_type
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, new_price):
        self.__price ={new_price}
    @type.setter
    def type(self, new_type):
        self.__type = new_type
    @property
    def content(self):
        return self.__content   
    @content.setter
    def content(self, cont):
        self.__content.pop()
        self.__content.append(cont)
    @property
    def category(self):
        return self.__category    
    @category.setter
    def category(self, cat):
        self.__category.pop()
        self.__category.append(cat)
    @property
    def dimension(self):
        return self.__dimension    
    @dimension.setter
    def dimension(self, dim):
        self.__dimension.pop()
        self.__dimension.append(dim)
    @property
    def order_status(self):
        return self.__order_status    
    def add_order_status(self, new_status):
        self.__order_status = new_status
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, new_addr):
        self.__address = new_addr
    @property
    def domiciliary(self):
        return self.__domiciliary
    @domiciliary.setter
    def domiciliary(self, new_dom):
        self.__domiciliary = new_dom

    def __str__(self):
        return (f"Paquete: {self.__name}\n"
                f"precio: {self.__price}\n"
                f"Peso: {self.__weight}\n"
                f"Tipo: {self.__type}\n"
                f"Contenido: {', '.join(self.__content) if self.__content else 'N/A'}\n"
                f"Categoría: {', '.join(self.__category) if self.__category else 'N/A'}\n"
                f"Dimensiones: {', '.join(self.__dimension) if self.__dimension else 'N/A'}\n"
                f"estado del pedido: {self.__order_status}\n")                

if __name__== "main":
    from excel_creation import ExcelPackages
    from creation_a import Creation
    package = Creation.create_packages()  
    ExcelPackages.save(package) 
