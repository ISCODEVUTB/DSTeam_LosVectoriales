import pytest
import os
from unittest.mock import patch, mock_open
from source.users_packages import register_user, authenticate_user
from source.management_p import Packages
from source.excel_creation import ExcelPackages
from source.management_e import place_order

test_users_file = "test_users.txt"
test_excel_file = "test_packages.xlsx"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Configura archivos de prueba y los elimina después de la ejecución."""
    if os.path.exists(test_users_file):
        os.remove(test_users_file)
    if os.path.exists(test_excel_file):
        os.remove(test_excel_file)
    yield
    if os.path.exists(test_users_file):
        os.remove(test_users_file)
    if os.path.exists(test_excel_file):
        os.remove(test_excel_file)

@patch("builtins.input", side_effect=["testuser", "testpass", "cliente"])
@patch("builtins.open", new_callable=mock_open)
def test_register_user(mock_open, mock_input):
    register_user()
    mock_open.assert_called_with("users.txt", "a")
    mock_open().write.assert_called()

@patch("builtins.input", side_effect=["testuser", "wrongpass"])
@patch("builtins.open", mock_open(read_data="testuser,5e88489f,cliente\n"))
def test_authenticate_user_fail(mock_open, mock_input):
    with patch("builtins.print") as mock_print:
        authenticate_user()
        mock_print.assert_called_with("Usuario o contrase\u00f1a incorrectos.")

def test_package_creation():
    package = Packages(name="Laptop", weight=2.5, price=1200, type="Electronics")
    assert package.name == "Laptop"
    assert package.weight == "2.5 kg"
    assert package.price == 1200
    assert package.type == "Electronics"

@patch("source.excel_creation.openpyxl.Workbook.save")
def test_save_package(mock_save):
    package = Packages(name="Laptop", weight=2.5, price=1200, type="Electronics")
    ExcelPackages.FILE_PATH = test_excel_file
    ExcelPackages.save(package)
    mock_save.assert_called()

@patch("builtins.input", side_effect=["Paquete 1"])
@patch("builtins.print")
def test_place_order(mock_print, mock_input):
    place_order("testuser")
    mock_print.assert_any_call("Pedido de 'Paquete 1' realizado con \u00e9xito.")
