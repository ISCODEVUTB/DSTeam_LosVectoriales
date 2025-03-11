class Creation:
    @staticmethod
    def create_packages():
        from management_p import Packages
        name = input("Nombre del paquete: ")
        price= input("Digite el precio del paquete: ")
        weight = input("Peso (kg): ")
        type = None
        while type != "basico" or type != "estandar" or type != "dimensionado":
            print("El tipo debe ser basico, estandar o dimensionado") 
            type = input("Tipo (basico, estandar o dimensionado): ")
            if type == "basico" or type == "estandar" or type == "dimensionado":
                break
        content = input("Contenido (separado por comas): ").split(",") 
        category = input("Categorías (separadas por comas): ").split(",") 
        dimension = input("Dimensiones (ej: 10x20x30 cm): ").split(",")
        order_status = "pendiente"
        address= None
        domiciliary= None
        return Packages(name, weight, price, type, content, category, dimension, order_status, address, domiciliary)