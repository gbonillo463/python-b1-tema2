"""
Enunciado:
Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función 'sum_list_numbers', el parámetro debe ser nombrado correctamente, el
mismo debe recibir una lista.

Las buenas prácticas de programación de Python PEP8 las puedes encontrar en 
el siguiente enlace:
https://peps.python.org/pep-0008/

La función debe retornar la suma de los números encontrados en la lista.

Parámetro:
El parámetro debe recibir la siguiente lista de números y debe ser nombrado
bajo las buenas prácticas de programación. Recibe la siguiente lista:
[50, 10.5, 21, 37.2, 99.9, 40.75, 80]

Ejemplo:
    Entrada:
    sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])

    Salida:
    339.35

"""


def sum_list_numbers(list_numbers):
    sum_num = 0
    for num in list_numbers:
        sum_num += num
    return sum_num


# Si quieres probar tu código, descomenta las siguientes líneas y
# ejecuta el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

print(sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]))
