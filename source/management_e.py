def place_order(usuario):
    from excel_creation import ExcelPackages
    print("\nLista de paquetes disponibles:")
    ExcelPackages.show_dis()
    
    packages = input("Ingrese el nombre del paquete que desea pedir: ")

    print(f"Pedido de '{packages}' realizado con éxito.")
