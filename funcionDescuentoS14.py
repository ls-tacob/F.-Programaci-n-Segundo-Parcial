def calcular_iva(subtotal, porcentaje_iva=13):
    valor_iva = (subtotal * porcentaje_iva) / 100
    return valor_iva

def descuento(total, porcentaje_descuento=10):
    valor_descuento = (total * porcentaje_descuento) / 100
    return valor_descuento

subtotal = float(input("Ingrese el monto total de la compra: "))

valor_iva = calcular_iva(subtotal)
total = subtotal + valor_iva

print(f'El valor del IVA es: {valor_iva}')
print(f'El valor total a cancelar es: {total}')

# Llamada a calcular_descuento con solo el monto total de la compra
total_con_descuento_1 = total - descuento(total)
print(f'Su total a pagar con un descuento del 10% es: {total_con_descuento_1}')

# Pide nuevamente el monto total de la compra antes de la segunda llamada
subtotal = float(input("Ingrese el monto total de la compra nuevamente: "))

# Llamada a calcular_descuento con el monto total de la compra y el porcentaje de descuento proporcionado por el usuario
porcentaje_descuento_opcional = input("Ingrese el porcentaje de descuento (deje vacío para utilizar el 10% por defecto): ")
porcentaje_descuento = int(porcentaje_descuento_opcional) if porcentaje_descuento_opcional else 10
total_con_descuento_2 = total - descuento(total, porcentaje_descuento)
print(f'Su total a pagar con un descuento del {porcentaje_descuento}% es: {total_con_descuento_2}')
