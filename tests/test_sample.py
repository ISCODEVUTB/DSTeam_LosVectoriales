import unittest
import sys
import os
import openpyxl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "source")))

from source.excel_creation import ExcelPackages
from source.management_p import Packages
import source.creation_a
import source.main
import source.management_e
import source.menu_u
import source.users_packages

class TestPackages(unittest.TestCase):
    def setUp(self):
        self.package = Packages("Box 1", "2", "50", "basic", ["Book"], ["Education"], ["10x10x10 cm"], "pending")

    def test_package_creation(self):
        self.assertEqual(self.package.name, "Box 1")
        self.assertEqual(self.package.weight, "2 kg")
        self.assertEqual(self.package.price, "50")
        self.assertEqual(self.package.type, "basic")
        self.assertEqual(self.package.content, ["Book"])
        self.assertEqual(self.package.category, ["Education"])
        self.assertEqual(self.package.dimension, ["10x10x10 cm"])
        self.assertEqual(self.package.order_status, "pending")

    def test_modify_package(self):
        self.package.name = "Box 2"
        self.package.weight = "3"
        self.package.content = ["Notebook"]  # Se mantiene correctamente como lista
        self.package.category = ["Office"]  # Se mantiene correctamente como lista
        self.package.dimension = ["20x20x20 cm"]  # Se mantiene correctamente como lista
        self.package.order_status = "shipped"

        self.assertEqual(self.package.name, "Box 2")
        self.assertEqual(self.package.weight, "3 kg")
        self.assertEqual(self.package.content, ["Notebook"])  # Ahora se compara correctamente
        self.assertEqual(self.package.category, ["Office"])
        self.assertEqual(self.package.dimension, ["20x20x20 cm"])
        self.assertEqual(self.package.order_status, "shipped")

class TestExcelPackages(unittest.TestCase):
    FILE_PATH = "test_packages.xlsx"

    @classmethod
    def setUpClass(cls):
        ExcelPackages.FILE_PATH = cls.FILE_PATH
        cls.package = Packages("Box Test", "1", "50", "standard", ["Mouse"], ["Technology"], ["5x5x5 cm"], "pending")
        ExcelPackages.start_excel(cls.package)

    def test_save_packages(self):
        package = Packages("Box Test", "1", "50", "standard", ["Mouse"], ["Technology"], ["5x5x5 cm"], "pending")
        ExcelPackages.save(package)

        wb = openpyxl.load_workbook(self.FILE_PATH)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        wb.close()

        expected_row = ("Box Test", "1 kg", "50", "standard", "Mouse", "Technology", "5x5x5 cm", "pending")
        self.assertEqual(data[1], expected_row)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)

# ✅ Test extra para verificar que pytest los detecta
def test_pytest_detection():
    assert True

if __name__ == "__main__":
    unittest.main()
