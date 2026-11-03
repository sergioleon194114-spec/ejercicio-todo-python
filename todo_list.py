# Aplicación de Lista de Tareas (To-Do List)

tareas = []

def mostrar_menu():
    print("\n==================================")
    print("     APLICACIÓN DE TAREAS")
    print("==================================")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    print("==================================")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ").strip()
    
    if opcion == '1':
        print("\n--- TUS TAREAS PENDIENTES ---")
        if not tareas:
            print("No hay tareas en la lista actualmente.")
        else:
            for indice, tarea in enumerate(tareas, start=1):
                print(f"{indice}. {tarea}")
                
    elif opcion == '2':
        nueva_tarea = input("Escribe la tarea que deseas agregar: ").strip()
        if nueva_tarea:
            tareas.append(nueva_tarea)
            print(f" Tarea '{nueva_tarea}' agregada con éxito.")
        else:
            print(" La tarea no puede estar vacía.")
            
    elif opcion == '3':
        if not tareas:
            print("\nNo hay tareas para eliminar.")
        else:
            print("\n--- TUS TAREAS PENDIENTES ---")
            for indice, tarea in enumerate(tareas, start=1):
                print(f"{indice}. {tarea}")
            
            try:
                num = int(input("Introduce el número de la tarea que deseas eliminar: "))
                if 1 <= num <= len(tareas):
                    eliminada = tareas.pop(num - 1)
                    print(f" Tarea '{eliminada}' eliminada correctamente.")
                else:
                    print(" Número de tarea fuera de rango.")
            except ValueError:
                print(" Por favor, introduce un número válido.")
                
    elif opcion == '4':
        print("\n¡Gracias por usar la aplicación de tareas! Hasta luego.")
        break
    else:
        print(" Opción no válida. Por favor elige un número entre 1 y 4.")