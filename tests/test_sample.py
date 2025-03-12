import unittest
import openpyxl
from source.management_p import Packages
from source.excel_creation import ExcelPackages

class TestPackages(unittest.TestCase):
    def setUp(self):
        self.package = Packages("Box 1", "2", "5", "express", ["Book"], ["Education"], ["10x10x10 cm"], "pending")

    def test_modify_package(self):
        self.package.name = "Box 2"
        self.package.weight = "3"
        self.package.content = "Notebook"  # Asegurar lista plana
        self.package.category = ["Office"]
        self.package.dimension = ["20x20x20 cm"]
        self.package.order_status = "shipped"

        self.assertEqual(self.package.name, "Box 2")
        self.assertEqual(self.package.weight, "3 kg")
        self.assertEqual(self.package.content, "Notebook")  # Se mantiene como lista simple
        self.assertEqual(self.package.category, ["Office"])
        self.assertEqual(self.package.dimension, ["20x20x20 cm"])
        self.assertEqual(self.package.order_status, "shipped")

class TestExcelPackages(unittest.TestCase):
    def test_save_packages(self):
        package = Packages("Box Test", "1", "50", "standard", "Mouse", ["Technology"], ["5x5x5 cm"], "pending")
        ExcelPackages.save(package)

        wb = openpyxl.load_workbook(ExcelPackages.FILE_PATH)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        wb.close()

        # Revisar última fila en el archivo para evitar fallos si hay otras entradas previas
        last_row = data[-1]  # Última entrada añadida

        expected_row = ("Box Test", "50", "1 kg", "standard", "Mouse", "Technology", "5x5x5 cm", "pending", "N/A", "N/A")
        self.assertEqual(last_row[:10], expected_row)  # Comparar solo los primeros 10 elementos
