import unittest
from source.main import management_p
from source.main import excel_creation
import os
import openpyxl

class TestPackage(unittest.TestCase):
    def setUp(self):
        self.package = Package("Box 1", "2", "basic", ["Book"], ["Education"], ["10x10x10 cm"], "pending")

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
        self.package.content.append("Notebook")
        self.package.category.append("Office")
        self.package.dimension.append("20x20x20 cm")
        self.package.order_status = "shipped"

        self.assertEqual(self.package.name, "Box 2")
        self.assertEqual(self.package.weight, "3 kg")
        self.assertIn("Notebook", self.package.content)
        self.assertIn("Office", self.package.category)
        self.assertIn("20x20x20 cm", self.package.dimension)
        self.assertEqual(self.package.order_status, "shipped")

class TestExcelPackage(unittest.TestCase):
    FILE_PATH = "test_packages.xlsx"

    @classmethod
    def setUpClass(cls):
        ExcelPackages.FILE_PATH = cls.FILE_PATH
        ExcelPackages.start_excel()

    def test_save_package(self):
        package = Package("Box Test", "1", "standard", ["Mouse"], ["Technology"], ["5x5x5 cm"], "pending")
        ExcelPackages.save(package)

        wb = openpyxl.load_workbook(self.FILE_PATH)
        ws = wb.active
        data = list(ws.iter_rows(values_only=True))
        wb.close()

        self.assertEqual(data[1], ("Box Test", "1 kg", "standard", "Mouse", "Technology", "5x5x5 cm", "pending"))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.FILE_PATH):
            os.remove(cls.FILE_PATH)

# ✅ Test extra para verificar que pytest los detecta
def test_pytest_detection():
    assert True

if __name__ == "__main__":
    unittest.main()
