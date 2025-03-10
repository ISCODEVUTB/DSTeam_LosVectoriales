from source.management_p import ExcelPaquetes

def hacer_pedido(usuario):
    print("\nLista de paquetes disponibles:")
    ExcelPaquetes.mostrar_dis()
    
    paquete = input("Ingrese el nombre del paquete que desea pedir: ")

    print(f"Pedido de '{paquete}' realizado con éxito.")
