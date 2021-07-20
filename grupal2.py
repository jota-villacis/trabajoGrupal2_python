'''

DESARROLLO

Considerando los avances realizados en nuestro proyecto, se solicita crear y agregar sentencias que nos permitan manipular un stock de productos. 
Para ello debemos aplicar lo siguiente:

- Definir el stock de un producto en una variable.
- Definir una forma de solicitar el stock disponible del producto por consola.
- Definir una forma de solicitar unidades del producto por consola. Este número de productos se almacenarán en una nueva variable llamada ‘Productos seleccionados’.
- Los productos reubicados serán descontados del stock inicial.
- El programa debe verificar que existan unidades disponibles.
- Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen más de 12 unidades. Verificar que el stock posibilite entregar 
una unidad extra. Sino se entregan las unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
- No se pueden solicitar más de 20 unidades en un mismo pedido.
- Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no es posible realizar esta acción debido a que no hay stock suficiente.
* El código debe estar debidamente comentado para asegurar su comprensión.

'''

# 1.Definir el stock de un producto en una variable
stock_producto = 50

# 2.Definir una forma de solicitar el stock disponible del producto por consola
# 3.- Definir una forma de solicitar unidades del producto por consola. Este número de productos se almacenarán en una nueva variable 
# llamada ‘Productos seleccionados’
# 4.Los productos reubicados serán descontados del stock inicial
# 5. El programa debe verificar que existan unidades disponibles.
# 6. Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen más de 12 unidades. Verificar que el stock posibilite entregar 
# una unidad extra. Sino se entregan las unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
# 7. No se pueden solicitar más de 20 unidades en un mismo pedido.
# 8. Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no es posible realizar esta acción debido a que no hay stock suficiente.

print(
    '''\n..:: Menú ::..\n
1) Ver stock disponible del producto
2) Solicitar unidades del producto

0) Salir
'''
)
# Control de excepcion en opción del menú
while True:
    try:
        opcion = int(input("Ingrese opción: "))
        break
    except ValueError:
        print("Opción ingresada no valida, vuelva a ingresarla opción")
    
if opcion == 1:
    print(f'El stock del producto es de: {stock_producto}')
elif opcion == 2:
    while True:
        try:
            productos_seleccionados = int(input("Unidades requeridas: "))
            break
        except ValueError:
            print("Opción ingresada no valida, vuelva a ingresarla opción")
    if productos_seleccionados > 20:
        print('No se pueden solicitar mas de 20 unidades por pedido')
    else:
        if productos_seleccionados - stock_producto <= 0:
            if productos_seleccionados > 12 and productos_seleccionados + 1 - stock_producto <= 0:
                productos_seleccionados = productos_seleccionados + 1
                print('Al llevar mas de 12 llevas 1 de regalo')
                stock_producto = stock_producto - productos_seleccionados
                print(f'El stock restante es de: {stock_producto}')
            else:
                stock_producto = stock_producto - productos_seleccionados
                print(f'El stock restante es de: {stock_producto}')
        else:
            print(f"Solicitaste {productos_seleccionados} y en stock hay disponible {stock_producto}")

elif opcion == 0:
    print("Programa Terminado")
else:
    print("Opción no válida")
