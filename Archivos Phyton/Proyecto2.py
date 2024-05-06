import json

# Base de datos simulada en memoria
cursos = {}
alumnos = {}
calificaciones = {}

# Funciones para el sistema de creación de cursos
def crear_curso():
    id_curso = input("Ingresa el ID del curso: ")
    if id_curso in cursos:
        print("El curso ya existe.")
        return
    nombre = input("Ingresa el nombre del curso: ")
    horario = input("Ingresa el horario del curso: ")
    salon = input("Ingresa el salón del curso: ")
    catedratico = input("Ingresa el nombre del catedrático: ")
    cursos[id_curso] = {
        "nombre": nombre,
        "horario": horario,
        "salon": salon,
        "catedratico": catedratico
    }
    print("Curso creado exitosamente.")

def editar_curso():
    listar_cursos()
    id_curso = input("Ingresa el ID del curso a editar: ")
    if id_curso not in cursos:
        print("El curso no existe.")
        return
    nombre = input("Ingresa el nuevo nombre del curso: ")
    horario = input("Ingresa el nuevo horario del curso: ")
    salon = input("Ingresa el nuevo salón del curso: ")
    catedratico = input("Ingresa el nuevo nombre del catedrático: ")
    cursos[id_curso] = {
        "nombre": nombre,
        "horario": horario,
        "salon": salon,
        "catedratico": catedratico
    }
    print("Curso editado exitosamente.")

def listar_cursos():
    for id_curso, info_curso in cursos.items():
        print(f"ID: {id_curso}, Nombre: {info_curso['nombre']}, Horario: {info_curso['horario']}, Salón: {info_curso['salon']}, Catedrático: {info_curso['catedratico']}")

# Funciones para el sistema de alumnos
def crear_alumno():
    carne = input("Ingresa el carné del alumno: ")
    if carne in alumnos:
        print("El alumno ya existe.")
        return
    nombre = input("Ingresa el nombre del alumno: ")
    fecha_nacimiento = input("Ingresa la fecha de nacimiento del alumno: ")
    alumnos[carne] = {
        "nombre": nombre,
        "fecha_nacimiento": fecha_nacimiento
    }
    print("Alumno creado exitosamente.")

def editar_alumno():
    listar_alumnos()
    carne = input("Ingresa el carné del alumno a editar: ")
    if carne not in alumnos:
        print("El alumno no existe.")
        return
    nombre = input("Ingresa el nuevo nombre del alumno: ")
    fecha_nacimiento = input("Ingresa la nueva fecha de nacimiento del alumno: ")
    alumnos[carne] = {
        "nombre": nombre,
        "fecha_nacimiento": fecha_nacimiento
    }
    print("Alumno editado exitosamente.")

def listar_alumnos():
    for carne, info_alumno in alumnos.items():
        print(f"Carné: {carne}, Nombre: {info_alumno['nombre']}, Fecha de nacimiento: {info_alumno['fecha_nacimiento']}")

# Funciones para el sistema de calificaciones
def asignar_calificacion():
    listar_cursos()
    id_curso = input("Selecciona el ID del curso: ")
    listar_alumnos()
    carne = input("Selecciona el carné del alumno: ")
    nota = float(input("Ingresa la nota del alumno: "))
    if id_curso not in calificaciones:
        calificaciones[id_curso] = {}
    calificaciones[id_curso][carne] = nota
    print("Calificación asignada exitosamente.")

# Funciones para el sistema de reportes
def reporte_cursos():
    reporte = {id_curso: len(info_curso) for id_curso, info_curso in calificaciones.items()}
    reporte_ordenado = dict(sorted(reporte.items(), key=lambda item: item[1], reverse=True))
    for id_curso, cantidad in reporte_ordenado.items():
        print(f"Curso: {cursos[id_curso]['nombre']}, Estudiantes: {cantidad}")

def reporte_estudiantes_curso():
    listar_cursos()
    id_curso = input("Selecciona el ID del curso: ")
    if id_curso not in calificaciones:
        print("No hay estudiantes en este curso.")
        return
    for carne, nota in calificaciones[id_curso].items():
        print(f"Alumno: {alumnos[carne]['nombre']}, Nota: {nota}")

def reporte_notas_alumno():
    listar_alumnos()
    carne = input("Selecciona el carné del alumno: ")
    for id_curso, notas in calificaciones.items():
        if carne in notas:
            print(f"Curso: {cursos[id_curso]['nombre']}, Nota: {notas[carne]}")

def reporte_promedio_cursos():
    for id_curso, notas in calificaciones.items():
        promedio = sum(notas.values()) / len(notas)
        print(f"Curso: {cursos[id_curso]['nombre']}, Promedio: {promedio}")

def reporte_mejor_desempeno():
    mejor_nota = 0
    mejor_alumno = ""
    for id_curso, notas in calificaciones.items():
        for carne, nota in notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_alumno = carne
    print(f"Mejor estudiante: {alumnos[mejor_alumno]['nombre']}, Nota: {mejor_nota}")

# Menú principal
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Crear/Editar Curso")
        print("2. Crear/Editar Alumno")
        print("3. Asignar Calificación")
        print("4. Reportes")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            subopcion = input("¿Deseas crear (c) o editar (e) un curso?: ")
            if subopcion == 'c':
                crear_curso()
            elif subopcion == 'e':
                editar_curso()
            else:
                print("Opción no válida.")
        elif opcion == '2':
            subopcion = input("¿Deseas crear (c) o editar (e) un alumno?: ")
            if subopcion == 'c':
                crear_alumno()
            elif subopcion == 'e':
                editar_alumno()
            else:
                print("Opción no válida.")
        elif opcion == '3':
            asignar_calificacion()
        elif opcion == '4':
            print("\nReportes")
            print("a. Listado de cursos con cantidad de estudiantes")
            print("b. Listar estudiantes y notas de un curso")
            print("c. Listar notas de un estudiante")
            print("d. Nota media por curso")
            print("e. Estudiante con mejor desempeño")
            subopcion = input("Selecciona un reporte: ")
            if subopcion == 'a':
                reporte_cursos()
            elif subopcion == 'b':
                reporte_estudiantes_curso()
            elif subopcion == 'c':
                reporte_notas_alumno()
            elif subopcion == 'd':
                reporte_promedio_cursos()
            elif subopcion == 'e':
                reporte_mejor_desempeno()
            else:
                print("Opción no válida.")
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()