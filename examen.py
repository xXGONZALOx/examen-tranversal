import random
import statistics
import csv

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = [0] * 10

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    bajos = []
    medios = []
    altos = []
    for i in range(10):
        if sueldos[i] < 800000:
            bajos.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] <= 2000000:
            medios.append((trabajadores[i], sueldos[i]))
        else:
            altos.append((trabajadores[i], sueldos[i]))
    
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(bajos)}")
    for nombre, sueldo in bajos:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(medios)}")
    for nombre, sueldo in medios:
        print(f"{nombre} ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(altos)}")
    for nombre, sueldo in altos:
        print(f"{nombre} ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def ver_estadisticas():
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    
    print(f"Sueldo más alto: ${sueldo_mas_alto}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica: ${media_geometrica}")

def reporte_sueldos():
    descuentos = [(sueldo * 0.07, sueldo * 0.12) for sueldo in sueldos]
    sueldos_liquidos = [sueldo - salud - afp for sueldo, (salud, afp) in zip(sueldos, descuentos)]
    
    with open("reporte_sueldos.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i in range(10):
            writer.writerow([trabajadores[i], sueldos[i], descuentos[i][0], descuentos[i][1], sueldos_liquidos[i]])
    
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
