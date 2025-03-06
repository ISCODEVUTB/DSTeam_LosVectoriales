import unittest
from GestionPaquetes.gestion_p import Paquetes, ExcelPaquetes
import os
import openpyxl

class TestPaquetes(unittest.TestCase):
    def setUp(self):
        self.paquete = Paquetes("Caja 1", "2", "basico", ["Libro"], ["Educación"], ["10x10x10 cm"], "pendiente")

    def test_creacion_paquete(self):
        self.assertEqual(self.paquete.nombre, "Caja 1")
        self.assertEqual(self.paquete.peso, "2")  # Se eliminó "kg" para evitar errores
        self.assertEqual(self.paquete.tipo, "basico")
        self.assertEqual(self.paquete.contenido, ["Libro"])
        self.assertEqual(self.paquete.categoria, ["Educación"])
        self.assertEqual(self.paquete.dimension, ["10x10x10 cm"])
        self.assertEqual(self.paquete.estado_pedido, "pendiente")

    def test_modificar_paquete(self):
        self.paquete.nombre = "Caja 2"
        self.paquete.peso = "3"
        self.paquete.contenido.append("Cuaderno")
        self.paquete.categoria.append("Oficina")
        self.paquete.dimension.append("20x20x20 cm")
        self.paquete.estado_pedido = "enviado"

        self.assertEqual(self.paquete.nombre, "Caja 2")
        self.assertEqual(self.paquete.peso, "3")  # Se eliminó "kg" para evitar errores
        self.assertIn("Cuaderno", self.paquete.contenido)
        self.assertIn("Oficina", self.paquete.categoria)
        self.assertIn("20x20x20 cm", self.paquete.dimension)
        self.assertEqual(self.paquete.estado_pedido, "enviado")

class TestExcelPaquetes(unittest.TestCase):
    FILE_PATH = "test_paquetes.xlsx"

    @classmethod
    def setUpClass(cls):
        ExcelPaquetes.FILE_PATH = cls.FILE_PATH
        ExcelPaquetes.iniciar_excel()

    def test_guardar_paquete(self):
        paquete = Paquetes("Caja Test", "1", "estandar", ["Mouse"], ["Tecnología"], ["5x5x5 cm"], "pendiente")
        ExcelPaquetes.guardar(paquete)

        wb = openpyxl.load_workbook(self.FILE_PATH)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        wb.close()

        print(data)  # Debugging line to check what is being saved
        self.assertEqual(data[1], ("Caja Test", "1", "estandar", "Mouse", "Tecnología", "5x5x5 cm", "pendiente"))

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.FILE_PATH)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()

