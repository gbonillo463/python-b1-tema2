"""
Enunciado:
Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función 'check_leap_year', el parámetro debe ser nombrado correctamente y
recibe como dato un año y mediante la función se debe retornar si este año es
bisiesto o no.

Para comprobar el año bisiesto fácilmente se puede utilizar la
operación mod '%', el resultado de la operación del año a consultar mod 4
debe ser igual a '0' y además el año a consultar mod 100 debe ser distinto de
'0'.

En el caso de obtener un resultado de '0' al realizar la operación del año
mod 100 se debe comprobar si el mismo año mod 400 es igual a '0'.

Parámetros:
El parámetro debe ser nombrado correctamente recibe como dato un valor de tipo
int.

Ejemplo:
El año a comprobar será '2000', por lo que:

2000 % 4 = 0        - Cumple un parámetro para ser considerado año bisiesto.

2000 % 100 = 0      - Como se obtuvo '0' se debe comprobar adicionalmente, que
                      el resultado del año a comprobar mod 400 sea '0' para
                      considerar que sea un año bisiesto.
2000 % 400 = 0      - El año '2000' si es un año bisiesto.

"""


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (
        year % 4 == 0 and year % 100 == 0 and year % 400 == 0
    ):
        return True
    else:
        return False


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el
# script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

print(check_leap_year(2024))
