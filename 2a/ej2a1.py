"""
Enunciado:
Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces 
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones 'sum_even_numbers_in_list_while(list_numbers)', 
'sum_even_numbers_in_list_for(list_numbers)' y
'sum_even_numbers_in_list_do_while(list_numbers)' en donde su parámetro
sea una lista de números y utilice un bucle 'WHILE', 'FOR' y 'DO WHILE', respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

Parámetros:
    list_numbers (List): lista de precios que se desea sumar

Ejemplo:
    Entrada:
    shopping_list = [10, 449, 33, 44, 188, 640]
    sum_even_numbers_in_list_while(shopping_list)
    sum_even_numbers_in_list_for(shopping_list)
    sum_even_numbers_in_list_do_while(shopping_list)

    Salida:
    En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640. 

"""

def sum_even_numbers_in_list_while(list_numbers):

    i = 0
    result = 0

    while i < len(list_numbers):
        if list_numbers[i] % 2 == 0:
            result += list_numbers[i]
        i += 1
    
    return result

def sum_even_numbers_in_list_for(list_numbers):

    result = 0

    for i in list_numbers:
        if i % 2 == 0:
            result += i

    return result

def sum_even_numbers_in_list_do_while(list_numbers):

    result = 0
    i = 0
    len_list = len(list_numbers)

    while True:
        if list_numbers[i] % 2 == 0:
            result += list_numbers[i] 
        i += 1
        if i >= len_list:
            break
        
    return result

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

shopping_list = [10, 449, 33, 44, 188, 640]
print(sum_even_numbers_in_list_while(shopping_list))
print(sum_even_numbers_in_list_for(shopping_list))
print(sum_even_numbers_in_list_do_while(shopping_list))
