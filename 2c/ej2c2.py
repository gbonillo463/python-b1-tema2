"""
Enunciado:
Imagina que trabajas en una aplicación de gestión de inventarios. Para obtener
información sobre un producto, es necesario buscarlo en una lista. Sin embargo, 
podría generarse un error si se ingresa un índice fuera del rango de la lista.
Así que debes manejar las excepciones.

Implementa 'get_element_from_list(items_list, index)' que reciba una lista
y un índice, y retorne el elemento de la lista correspondiente al índice. Si
el índice está fuera del rango de la lista, la función debe retornar "The
specified index is out of the list's range". En caso de un error inesperado, ha
de retornar "An unexpected error has occurred: {error}".

Parámetros:
items_list (List): Lista de la que se desea obtener el elemento.
index (int): Índice del elemento que se desea obtener.

Ejemplo:
    Entrada:
    get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3)
    get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5)
    
    Salida:
    - En el primer caso el resultado es: "Notebook"
    - En el segundo caso el resultado es: "The specified index is out of the items_list's range"
    - En caso de un error inesperado, ha de retornar: "An unexpected error has occurred: {error}"
    
"""


def get_element_from_list(items_list, index) -> str:
    try:
        return items_list[index]
    except IndexError:
        return "The specified index is out of the items_list's range"
    except Exception as e:
        return f'An unexpected error has occurred: {e}'


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3))
print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5))
