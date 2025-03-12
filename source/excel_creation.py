import openpyxl

class ExcelPackages:
    FILE_PATH = "packages.xlsx"

    @staticmethod
    def save(package):
        try:
            wb = openpyxl.load_workbook(ExcelPackages.FILE_PATH)
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            wb.active.append(["Name", "Price", "Weight", "Type", "Content", "Category", "Dimension", "Order Status", "Address", "Courier"])
        
        ws = wb.active

        row = [
            package.name,
            package.price,
            package.weight,
            package.type,
            ", ".join(package.content) if isinstance(package.content, list) else package.content,
            ", ".join(package.category) if isinstance(package.category, list) else package.category,
            ", ".join(package.dimension) if isinstance(package.dimension, list) else package.dimension,
            package.order_status,
            "N/A",  # Dirección
            "N/A"   # Domiciliario
        ]
        
        ws.append(row)
        wb.save(ExcelPackages.FILE_PATH)
