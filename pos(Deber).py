carrito = []
total = 0.0

def mostrar_menu():
    print("1. Agregar producto 🛒")
    print("2. Ver el total 🧿")
    print("3. Pagar 💲")
    print("4. Quitar producto 🫳")
    print("5. Salir ❌")

def agregar_producto():
    global total
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    print("")
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"Se agrego el producto {producto} con exito 👍")
    print(f"El precio del procducto es de {precio:.2f}$")
    print("")

def ver_total():
    print(f"El total de sus productos es de {total:.2f}$")

def pagar():
    global total, carrito
    if total == 0:
        print("No tienes ningun producto que pagar")
    else:
        print(f"El total que va a pagar es de {total:.2f}$")
        pago = float(input("Ingrese la cantidad que se va a pagar: "))
        if pago == total:
            print("Pago realizado con exito")
            print("")
            
            carrito = []
            total = 0.0
        elif pago > total:
            cambio = pago - total
            print(f"Pago realizado, su cambio es de {cambio:.2f}$")
            print("")
            
            carrito = []
            total = 0.0   
        else:
            print("No tiene suficiente dinaro para pagar.")
            print("")

def elimiar_producto():
    global total
    if not carrito:
        print("No tienes productos")
    else:
        prodcuto_eliminar = input("Ingrese el nombre del producto que eliminara: ")
        for producto in carrito:
            if producto["producto"] == prodcuto_eliminar:
                carrito.remove(producto)
                total -= producto["precio"]
                print("")
                print("Producto eliminado")
        else:
            print("")
            print("No se ha encontrado ese producto")

def ejecutar():
    while True:
        print("")
        print("-" * 27, "Punto de venta", "-" * 27)
        mostrar_menu()
        opcion = input("Escoja una de las opciones: ")
        print("-" * 70)
        print("")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_total()
        elif opcion == '3':
            pagar()
        elif opcion == '4':
            elimiar_producto()
        elif opcion == '5':
            print("Saliendo del sistema...")
            print("")
            break
        else:
            print("Opcion no valida")

ejecutar()   