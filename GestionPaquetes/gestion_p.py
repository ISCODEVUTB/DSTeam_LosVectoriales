import openpyxl
import os

class Paquetes:
    def __init__(self, nombre, peso, tipo, contenido=None, categoria=None, dimension=None):
        self.__nombre = nombre
        self.__peso = f"{peso} kg"
        self.__tipo = tipo
        self.__contenido = contenido if contenido else []
        self.__categoria = categoria if categoria else []
        self.__dimension = dimension if dimension else []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_name):
        self.__nombre = new_name

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, new_peso):
        self.__peso = f"{new_peso} kg"

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, new_tipo):
        self.__tipo = new_tipo

    @property
    def contenido(self):
        return self.__contenido
    
    def agregar_contenido(self, cont):
        self.__contenido.append(cont)

    @property
    def categoria(self):
        return self.__categoria
    
    def agregar_categoria(self, cat):
        self.__categoria.append(cat)

    @property
    def dimension(self):
        return self.__dimension
    
    def agregar_dimension(self, dim):
        self.__dimension.append(dim)

    def __str__(self):
        return (f"Paquete: {self.__nombre}\n"
                f"Peso: {self.__peso}\n"
                f"Tipo: {self.__tipo}\n"
                f"Contenido: {', '.join(self.__contenido) if self.__contenido else 'N/A'}\n"
                f"Categoría: {', '.join(self.__categoria) if self.__categoria else 'N/A'}\n"
                f"Dimensiones: {', '.join(self.__dimension) if self.__dimension else 'N/A'}\n")

class Creacion:
    @staticmethod
    def crear_paquete():
        nombre = input("Nombre del paquete: ")
        peso = input("Peso (kg): ")
        tipo = None
        while tipo != "basico" or tipo != "estandar" or tipo != "dimensionado":
            print("El tipo debe ser basico, estandar o dimensionado") 
            tipo = input("Tipo (basico, estandar o dimensionado): ")
            if tipo == "basico" or tipo == "estandar" or tipo == "dimensionado":
                break
        contenido = input("Contenido (separado por comas): ").split(",") 
        categoria = input("Categorías (separadas por comas): ").split(",") 
        dimension = input("Dimensiones (ej: 10x20x30 cm): ").split(",")

        return Paquetes(nombre, peso, tipo, contenido, categoria, dimension)

paquete = Creacion.crear_paquete()
print("\nPaquete creado con éxito:\n")
print(paquete)

#creacion base de datos
class Paquetes:
    FILE_PATH = "paquetes.xlsx"
    @classmethod

    def iniciar_excel(cls):
        if not os.path.exists(cls.FILE_PATH):
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(["Nombre", "Peso", "Tipo", "Contenido", "Categoría", "Dimensiones"])
            wb.save(cls.FILE_PATH)
    def to_list(self):
        return [self.nombre, self.peso, self.tipo, self.contenido, self.categoria, self.dimension]
    
    @classmethod
    def guardar(cls, paquete):
        wb = openpyxl.load_workbook(cls.FILE_PATH)
        ws = wb.active
        ws.append(paquete.to_list())
        wb.save(cls.FILE_PATH)

    @classmethod
    def mostrar(cls):
        """Muestra los paquetes almacenados en el archivo Excel."""
        wb = openpyxl.load_workbook(cls.FILE_PATH)
        ws = wb.active
        if ws.max_row == 1:
            print("No hay paquetes guardados.")
            return
        print("Paquetes almacenados:\n")
        for row in ws.iter_rows(min_row=2, values_only=True):
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
    @classmethod
    def crear(cls):
        nombre = input("Nombre: ")
        peso = input("Peso (kg): ")
        tipo = input("Tipo (basico, estandar, dimensionado): ").strip().lower()
        while tipo not in ["basico", "estandar", "dimensionado"]:
            print("Tipo inválido. Debe ser basico, estandar o dimensionado.")
            tipo = input("Tipo: ").strip().lower()
        contenido = input("Contenido (separado por comas): ")
        categoria = input("Categoría (separada por comas): ")
        dimension = input("Dimensiones (ej: 10x20x30 cm): ")

        paquete = cls(nombre, peso, tipo, contenido, categoria, dimension)
        cls.guardar(paquete)
        print("\n Paquete guardado correctamente.")
        return paquete

Paquetes.inicializar_excel()

paquete = Paquetes.crear()
print("\n Paquete creado:\n", paquete.to_list())

Paquetes.mostrar()
