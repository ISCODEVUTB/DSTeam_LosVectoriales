import unittest
from GestionPaquetes.gestion_p import Paquetes, ExcelPaquetes
import os
import openpyxl

class TestPaquetes(unittest.TestCase):
    def setUp(self):
        self.paquete = Paquetes("Caja 1", "2", "basico", ["Libro"], ["Educación"], ["10x10x10 cm"], "pendiente")

    def test_creacion_paquete(self):
        self.assertEqual(self.paquete.nombre, "Caja 1")
        self.assertEqual(self.paquete.peso, "2 kg")
        self.assertEqual(self.paquete.tipo, "basico")
        self.assertEqual(self.paquete.contenido, ["Libro"])
        self.assertEqual(self.paquete.categoria, ["Educación"])
        self.assertEqual(self.paquete.dimension, ["10x10x10 cm"])
        self.assertEqual(self.paquete.estado_pedido, "pendiente")

    def test_modificar_paquete(self):
        self.paquete.nombre = "Caja 2"
        self.paquete.peso = "3"
        self.paquete.agregar_contenido("Cuaderno")
        self.paquete.agregar_categoria("Oficina")
        self.paquete.agregar_dimension("20x20x20 cm")
        self.paquete.agregar_estado_pedido("enviado")

        self.assertEqual(self.paquete.nombre, "Caja 2")
        self.assertEqual(self.paquete.peso, "3 kg")
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

        self.assertEqual(data[1], ("Caja Test", "1 kg", "estandar", "Mouse", "Tecnología", "5x5x5 cm", "pendiente"))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)

if _name_ == "_main_":
    unittest.main()
