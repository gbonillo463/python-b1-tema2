"""
Enunciado:
Se requiere crear dos funciones que trabajen con una lista de estudiantes
y agreguen un nuevo estudiante a la lista. La diferencia es que la función
'add_student_by_value(list_students, new_student)' debe agregar al nuevo
estudiante usando paso por valor y la función
'add_student_by_reference(list_students, new_student)' usando paso por
referencia. Ambas funciones serán orquestadas desde la función
'main(list_students, new_student)' la cual ya está definida.

La función 'add_student_by_value(list_students, new_student)' debe copiar
la lista de estudiantes para no afectar la lista original y agregar al nuevo
estudiante. Esta es la solución de paso por valor.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

La función 'add_student_by_reference(list_students, new_student)' debe agregar
al nuevo estudiante usando paso por referencia.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

La función 'main(list_students, new_student)' es la que llamará a las 2
funciones previamente definidas para comprobar que list_students
cambie de acuerdo a la función llamada.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

Ejemplo:
    Entrada:
    list_students = ['Alice', 'Bob', 'Juan']
    new_student_by_value = 'Maria'
    new_student_by_reference = 'Sofia'

    main(list_students, new_student_by_value, new_student_by_reference)

    Salida:
    Original student list ['Alice', 'Bob', 'Juan']
    Student list by value ['Alice', 'Bob', 'Juan', 'Maria']
    Student list by reference ['Alice', 'Bob', 'Juan', 'Sofia']
    Original student list ['Alice', 'Bob', 'Juan', 'Sofia']

"""


def add_student_by_value(list_students, new_student):
    
    new_list = list_students.copy()
    new_list.append(new_student)
    return new_list
    

def add_student_by_reference(list_students, new_student):
    
    list_students.append(new_student)
    return list_students


def main(list_students, new_student_by_value, new_student_by_reference):
    
    list_value = add_student_by_value(list_students, new_student_by_value)
    list_reference = add_student_by_reference(list_students, new_student_by_reference)
    
    return list_students
    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# list_students = ["Alice", "Bob", "Juan"]
# new_student_by_value = "Maria"
# new_student_by_reference = "Sofia"

# main(list_students, new_student_by_value, new_student_by_reference) 