import random
import csv
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”MiguelSánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = []
        
def generar_sueldo_aleatorio():
     sueldos = [random.randint(300000, 2500000) for _ in range(10)]
     return sueldos
 
def clasificar_sueldo():
    menor_800k = []
    entre_800k_2m = []
    mayor_2m = []

    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            menor_800k.append((nombre, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            mayor_2m.append((nombre, sueldo))
            
            print("sueldos menores a 800")
            print("total:",len("menor 800k"))
            for nombre, sueldo in menor_800k:
                print(f"{nombre} {sueldo}")
                print("sueldos entre $800 y $2.000.000")
                print("total", len("entre_800k_2m"))
                print(f"{nombre} {sueldo}")
                print("sueldos superiores a 2.000.000")
                print(nombre, sueldo in entre_800k_2m)
                print("total:", len("mayor_2m"))
                print(f"{nombre} {sueldo}")
                total_sueldos = sum(sueldos)
                print("total sueldos: $", total_sueldos)
                    
def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    prod = 1
    for sueldo in sueldos:
        prod *= sueldo
    media_geometrica = prod ** (1 / len(sueldos))
    for sueldo in sueldos:
        prod *= sueldo
    media_geometrica = prod ** (1 / len(sueldos))
    
    
    prod = 1
def menu():
    
 def generar_reporte_sueldos(sueldos):
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])

            print("Se ha generado el reporte de sueldos en 'reporte_sueldos.csv'.")
            print("---- Menú Principal ----")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                sueldos = generar_sueldos_aleatorios()
                print("Sueldos aleatorios asignados correctamente.")
            elif opcion == '2':
                clasificar_sueldos(sueldos)
            elif opcion == '3':
                ver_estadisticas(sueldos)
            elif opcion == '4':
                generar_reporte_sueldos(sueldos)
            elif opcion == '5':
                print("Saliendo del programa...")
            break
        else:
            print("ingrece opcion valida")