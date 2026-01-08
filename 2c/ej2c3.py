"""
Enunciado:
Imagina que estás trabajando en una aplicación para calcular factoriales. Crea
una función 'calculate_factorial(number)' que orquestará el proceso del cálculo
del factorial usando la función 'factorial(number)' que recibirá un número entero 
no negativo y calculará su factorial. Por lo tanto, debes manejar las excepciones 
para controlar que las funciones se utilizan correctamente.

De esta manera, 'calculate_factorial(number)' recibe un número entero y calcula su
factorial llamando a 'factorial(number)'. Si ocurre una excepción al invocar a 
'factorial(number)', debe mostrar el mensaje de error: "An unexpected error has 
occurred: {error}".

Parámetros:
number (int): El número del cual se desea calcular el factorial.

La función 'factorial(number)' calcula el factorial del número. Si el número
introducido es negativo debe lanzar una excepción con el mensaje "Factorial of
a negative number cannot be calculated".

Parámetros:
number (int): El número del cual se desea calcular el factorial.

Ejemplo:
    Entrada:
    calculate_factorial(5)
    calculate_factorial(-5)
    
    Salida:
    - En el primer caso el resultado es: 120
    - En el segundo caso se genera un error: "An unexpected error has occurred: Factorial of a
     negative number cannot be calculated"
    

"""


def factorial(number: int):
    if number < 0:
        raise ValueError("Factorial of a negative number cannot be calculated.")
    if number == 0:
        return 1
    return number * factorial(number - 1)


def calculate_factorial(number: int):
    try:
        return factorial(number)
    except Exception as e:
        return f'An unexpected error has occurred: {e}'

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(calculate_factorial(-5))