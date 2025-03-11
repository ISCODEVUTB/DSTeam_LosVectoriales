import unittest
import sys
import os
import openpyxl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "source")))

from excel_creation import ExcelPackages
from management_p import Packages

class TestPackages(unittest.TestCase):
    def setUp(self):
        self.package = Packages("Box 1", "2", "100", "basic", ["Book"], ["Education"], ["10x10x10 cm"], "pending")

    def test_package_creation(self):
        self.assertEqual(self.package.name, "Box 1")
        self.assertEqual(self.package.weight, "2 kg")
        self.assertEqual(self.package.type, "basic")
        self.assertEqual(self.package.content, ["Book"])
        self.assertEqual(self.package.category, ["Education"])
        self.assertEqual(self.package.dimension, ["10x10x10 cm"])
        self.assertEqual(self.package.order_status, "pending")

    def test_modify_package(self):
        self.package.name = "Box 2"
        self.package.weight = "3"
        self.package.content = ["Notebook"]
        self.package.category = ["Office"]
        self.package.dimension = ["20x20x20 cm"]
        self.package.add_order_status("shipped")

        self.assertEqual(self.package.name, "Box 2")
        self.assertEqual(self.package.weight, "3 kg")
        self.assertEqual(self.package.content, ["Notebook"])
        self.assertEqual(self.package.category, ["Office"])
        self.assertEqual(self.package.dimension, ["20x20x20 cm"])
        self.assertEqual(self.package.order_status, "shipped")

class TestExcelPackages(unittest.TestCase):
    FILE_PATH = "test_packages.xlsx"

    @classmethod
    def setUpClass(cls):
        ExcelPackages.FILE_PATH = cls.FILE_PATH
        ExcelPackages.start_excel()

    def test_save_packages(self):
        packages = Packages("Box Test", "1", "50", "standard", ["Mouse"], ["Technology"], ["5x5x5 cm"], "pending")
        ExcelPackages.save(packages)

        wb = openpyxl.load_workbook(self.FILE_PATH)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        wb.close()

        self.assertEqual(data[1], ("Box Test", "1 kg", "50", "standard", "Mouse", "Technology", "5x5x5 cm", "pending"))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)

# ✅ Test extra para verificar que pytest los detecta
def test_pytest_detection():
    assert True

if __name__ == "__main__":
    unittest.main()
