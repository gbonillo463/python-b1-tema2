from typing import List

"""
Enunciado:
Corrige la función 'division_list' que realiza una división de una lista
de número enteros dividido para un número escalar.

Para corregir los errores se puede cambiar los valores de la lista
'list_numbers' y el valor del número escalar 'scalar_number'.

En la función 'division_list' se debe verificar que el contenido de
la lista sea de tipo 'int' o 'float', caso contrario, mostrar una
excepción TypeError(f"Value {number_in_list} is not numeric.").

Parámetros:
    list_numbers (list): Lista de números.
    number (int): Número entero.
    
Ejemplos:
    Entrada:
        list_numbers = [1.5, 2.5, 9.2, 0, 22]
        scalar_number = 4.0
        
    Salida:
        [0.375, 0.625, 2.3, 0.0, 5.5]

"""


def division_list(list_numbers: List, number: int) -> List[float]:
    try:
        if not all(isinstance(num, (int, float)) for num in list_numbers):
            raise TypeError(f"Value is not numeric.")
        if number == 0:
            raise ZeroDivisionError("Scalar number can't be 0")
        
        else:
            result = []
            for number_in_list in list_numbers:
                result.append(number_in_list / float(number))
        return result
    except TypeError:
        raise TypeError
    except ZeroDivisionError:
        raise ZeroDivisionError
    
list_numbers = [1.5, 2.5, "9.2", 0, 22]
scalar_number = '4.0'

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(division_list(list_numbers, scalar_number))
