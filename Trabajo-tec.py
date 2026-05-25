import os
import csv
import matplotlib.pyplot as plt

# Usuarios y contraseñas válidos (esto es el login aca empieza el esqueleto del proyecto)
usuarios = {
    "Alexis": "4044",
    "Maria": "5678"
}

def login():
    print("Bienvenido al Sistema de Gastos Personales")
    print("-------------------------------------------")
    
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Acceso permitido. Bienvenido,", usuario)
        return usuario
    else:
        print("Usuario o contraseña incorrectos")
        return None

def verificar_csv():
    if not os.path.exists("gastos.csv"): #sirve para verificar si el archivo existe o no (aca nosotros queremos crear uno asi que no va a existir)
        archivo = open("gastos.csv", "w") #aca lo que hacemos es crear el archivo como "gastos.csv" y escribimos "w" que viene de write para crear el archivo que no existe
        archivo.write("usuario,monto,categoria\n") #la n aca es un salto de linea para que no quede pegado a la proxima linea (es mas un tema estético)
        archivo.close() #sirve para cerrar el archivo una vez que termines de usarlo, despues al momento de las funciones simplemente vamos a volverloa abrir
        print("Archivo de gastos creado correctamente")

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Modificar gasto")
    print("4. Eliminar gasto")
    print("5. Ver estadísticas")
    print("6. Recomendaciones automáticas")
    print("7. Salir")
    
    opcion = input("Seleccioná una opción: ")
    return opcion

# primera función
def agregar_gasto(usuario):
    monto = input("Monto: ") #aca ambos inputs son necesarios para que el usuario ingrese el monto y la categoria
    categoria = input("Categoría: ")
    
    archivo = open("gastos.csv", "a") #a de append para agregar sin borrar lo anterior
    archivo.write(usuario + "," + monto + "," + categoria + "\n") #la n nuevamente para separar las palabras
    archivo.close()
    
    print("Gasto agregado correctamente")

# segunda función
def ver_gastos(usuario):
    print("\n--- MIS GASTOS ---")
    
    archivo = open("gastos.csv", "r") #la r aca significa leer el archivo
    lector = csv.reader(archivo)
    next(lector)  # saltea la primera fila que son los títulos
    
    contador = 1
    for fila in lector:
        if fila[0] == usuario:
            print(contador, "-", fila[2], "- $" + fila[1]) #fila[0] es el usuario, fila[1] es el monto, fila[2] es la categoría. Solo muestra los gastos del usuario que está logueado
            contador += 1 # y este contador nos sirve para que en la interfaz se nos muestre una lista numerada.
    
    archivo.close()

# quinta función
def ver_estadisticas(usuario):
    print("\n--- ESTADÍSTICAS ---")
    
    archivo = open("gastos.csv", "r")
    lector = csv.reader(archivo)
    next(lector)
    
    montos = []
    categorias = []  # lista vacía para guardar las categorías
    
    for fila in lector:
        if fila[0] == usuario:
            montos.append(int(fila[1]))
            categorias.append(fila[2])  # agrega la categoría a la lista

    archivo.close()
    
    if len(montos) == 0:
        print("No tenés gastos registrados")
        return
    
    total = sum(montos)
    promedio = total // len(montos)
    maximo = max(montos)
    minimo = min(montos)
    
    print("Total gastado: $", total)
    print("Promedio: $", promedio)
    print("Mayor gasto: $", maximo)
    print("Menor gasto: $", minimo)
    
    # gráfico de barras con los gastos por categoría
    plt.bar(categorias, montos, color="blue") #crea el gráfico de barras. categorias va en el eje X (abajo) y montos en el eje Y (costado). color="blue" es simplemente el color de las barras.
    plt.title("Mis gastos por categoría") #le pone el título arriba del gráfico.
    plt.xlabel("Categoría") #le pone el texto abajo del eje X.
    plt.ylabel("Monto") #le pone el texto al costado del eje Y.
    plt.show() #muestra la ventana con el gráfico. Sin esta línea el gráfico no aparece.

# sexta función
def recomendaciones(usuario):
    print("\n--- RECOMENDACIONES ---")
    
    archivo = open("gastos.csv", "r")
    lector = csv.reader(archivo)
    next(lector)
    
    montos = []
    
    for fila in lector:
        if fila[0] == usuario:
            montos.append(int(fila[1]))
    
    # el for recorre todas las filas del CSV una por una. Por ejemplo si el CSV tiene esto:
    # alexis,5000,Comida
    # maria,3000,Transporte
    # josé,2000,Salud
    # el for pasa por las tres filas, pero el if fila[0] == usuario filtra y solo agarra las de alexis.

    archivo.close()
    
    if len(montos) == 0:
        print("No tenés gastos registrados")
        return
    
    total = sum(montos)
    promedio = total // len(montos)
    
    if total > 50000:
        print("⚠️ Alerta: tus gastos totales superaron los $50.000")
    
    if promedio > 10000:
        print("⚠️ Tu gasto promedio es alto, revisá tus gastos")
    
    if len(montos) > 10:
        print("⚠️ Tenés muchos gastos registrados este mes")
    
    if total <= 50000 and promedio <= 10000:
        print("✅ Tus gastos están bajo control")

# aca abajo va el código que ejecuta todo
usuario_activo = login()

if usuario_activo is None:
    print("Acceso denegado. Cerrando el programa.")
else:
    verificar_csv()
    while True:
        opcion = menu()
        
        if opcion == "1":
            agregar_gasto(usuario_activo)
        elif opcion == "2":
            ver_gastos(usuario_activo)
        elif opcion == "3":
            print("Para modificar un gasto, reiniciá el programa")
        elif opcion == "4":
            print("Para eliminar un gasto, reiniciá el programa")
        elif opcion == "5":
            ver_estadisticas(usuario_activo)
        elif opcion == "6":
            recomendaciones(usuario_activo)
        elif opcion == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo")