import os
import csv
import requests
import google.generativeai as genai
 
# API Keys
API_KEY_CLIMA = "fe167e6ae5b3af34ee87421d83e7bded"
API_KEY_GEMINI = "AIzaSyCn5jPTVE3aPWqR8mRDAaqSWmL8y_rbnP0"
 
# Archivos CSV
ARCHIVO_USUARIOS = "usuarios_simulados.csv"
ARCHIVO_HISTORIAL = "historial_global.csv"
 
# -------------------------
# FUNCIONES DE ARCHIVOS CSV
# -------------------------
 
def verificar_archivos():
    # Crea el archivo de usuarios si no existe
    if not os.path.exists(ARCHIVO_USUARIOS):
        archivo = open(ARCHIVO_USUARIOS, "w")
        archivo.write("username,password\n")
        archivo.close()
 
    # Crea el archivo de historial si no existe
    if not os.path.exists(ARCHIVO_HISTORIAL):
        archivo = open(ARCHIVO_HISTORIAL, "w")
        archivo.write("usuario,ciudad,temperatura,condicion,humedad,viento\n")
        archivo.close()
 
# -------------------------
# FUNCIONES DE USUARIOS
# -------------------------
 
def validar_contrasena(contrasena):
    # Criterios de seguridad para la contraseña
    errores = []
 
    if len(contrasena) < 8:
        errores.append("- Debe tener al menos 8 caracteres")
 
    if not any(c.isupper() for c in contrasena):
        errores.append("- Debe tener al menos una mayúscula")
 
    if not any(c.isdigit() for c in contrasena):
        errores.append("- Debe tener al menos un número")
 
    return errores
 
def usuario_existe(username):
    # Revisa si el usuario ya existe en el CSV
    archivo = open(ARCHIVO_USUARIOS, "r")
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        if fila[0] == username:
            archivo.close()
            return True
    archivo.close()
    return False
 
def registrar_usuario():
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
 
    # Pedir username
    username = input("Nombre de usuario: ").strip()
    if usuario_existe(username):
        print("Ese nombre de usuario ya existe. Intentá con otro.")
        return None
 
    # Pedir y validar contraseña
    while True:
        contrasena = input("Contraseña: ")
        errores = validar_contrasena(contrasena)
        if errores:
            print("Contraseña rechazada. No cumple con:")
            for e in errores:
                print(e)
            print("Sugerencia: usá algo como 'MiGasto2024' (mayúscula + número + 8 caracteres)")
        else:
            break
 
    # Guardar usuario en CSV
    archivo = open(ARCHIVO_USUARIOS, "a")
    archivo.write(username + "," + contrasena + "\n")
    archivo.close()
    print("Usuario registrado correctamente. Iniciando sesión...")
    return username
 
def iniciar_sesion():
    print("\n--- INICIAR SESIÓN ---")
    username = input("Usuario: ").strip()
    contrasena = input("Contraseña: ")
 
    archivo = open(ARCHIVO_USUARIOS, "r")
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        if fila[0] == username and fila[1] == contrasena:
            archivo.close()
            print("Acceso concedido. Bienvenido,", username)
            return username
    archivo.close()
    print("Usuario o contraseña incorrectos.")
    return None
 
# -------------------------
# FUNCIONES DE CLIMA
# -------------------------
 
def consultar_clima(ciudad):
    # Conectarse a la API de OpenWeatherMap
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ciudad,
        "appid": API_KEY_CLIMA,
        "units": "metric",
        "lang": "es"
    }
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        datos = respuesta.json()
 
        if respuesta.status_code == 404:
            print("Ciudad no encontrada.")
            return None
        if respuesta.status_code != 200:
            print("Error al consultar el clima.")
            return None
 
        # Extraer los datos importantes
        temperatura = datos["main"]["temp"]
        condicion = datos["weather"][0]["description"]
        humedad = datos["main"]["humidity"]
        viento = datos["wind"]["speed"]
 
        print("\n--- CLIMA EN", ciudad.upper(), "---")
        print("Temperatura:", temperatura, "°C")
        print("Condición:", condicion.capitalize())
        print("Humedad:", humedad, "%")
        print("Viento:", viento, "km/h")
 
        return {
            "ciudad": ciudad,
            "temperatura": temperatura,
            "condicion": condicion,
            "humedad": humedad,
            "viento": viento
        }
 
    except Exception as e:
        print("Error de conexión:", e)
        return None
 
def guardar_historial(usuario, datos_clima):
    # Guarda la consulta en el historial global CSV
    archivo = open(ARCHIVO_HISTORIAL, "a")
    archivo.write(
        usuario + "," +
        datos_clima["ciudad"] + "," +
        str(datos_clima["temperatura"]) + "," +
        datos_clima["condicion"] + "," +
        str(datos_clima["humedad"]) + "," +
        str(datos_clima["viento"]) + "\n"
    )
    archivo.close()
    print("Consulta guardada en el historial.")
 
# -------------------------
# FUNCIONES DE HISTORIAL Y ESTADÍSTICAS
# -------------------------
 
def ver_historial(usuario):
    print("\n--- MI HISTORIAL DE CONSULTAS ---")
    ciudad = input("¿Para qué ciudad querés ver el historial? ").strip()
 
    archivo = open(ARCHIVO_HISTORIAL, "r")
    lector = csv.reader(archivo)
    next(lector)
 
    encontrado = False
    for fila in lector:
        if fila[0] == usuario and fila[1].lower() == ciudad.lower():
            print("Ciudad:", fila[1], "| Temp:", fila[2], "°C | Condición:", fila[3], "| Humedad:", fila[4], "% | Viento:", fila[5], "km/h")
            encontrado = True
 
    archivo.close()
    if not encontrado:
        print("No hay consultas registradas para esa ciudad.")
 
def ver_estadisticas():
    print("\n--- ESTADÍSTICAS GLOBALES ---")
 
    archivo = open(ARCHIVO_HISTORIAL, "r")
    lector = csv.reader(archivo)
    next(lector)
 
    temperaturas = []
    ciudades = []
 
    for fila in lector:
        if len(fila) >= 3:
            ciudades.append(fila[1])
            temperaturas.append(float(fila[2]))
 
    archivo.close()
 
    if len(temperaturas) == 0:
        print("No hay consultas registradas todavía.")
        return
 
    ciudad_mas_consultada = max(ciudades, key=ciudades.count)
    total_consultas = len(temperaturas)
    temp_promedio = sum(temperaturas) / total_consultas
 
    print("Ciudad más consultada:", ciudad_mas_consultada)
    print("Total de consultas:", total_consultas)
    print("Temperatura promedio registrada:", round(temp_promedio, 1), "°C")
 
# -------------------------
# FUNCIÓN DE IA (GEMINI)
# -------------------------
 
def consejo_vestimenta(datos_clima):
    # Conectarse a Gemini y pedir un consejo de vestimenta según el clima
    try:
        genai.configure(api_key=API_KEY_GEMINI)
        model = genai.GenerativeModel("gemini-pro")
 
        prompt = (
            f"El clima actual es: temperatura {datos_clima['temperatura']}°C, "
            f"condición {datos_clima['condicion']}, humedad {datos_clima['humedad']}%, "
            f"viento {datos_clima['viento']} km/h. "
            f"Dame un consejo breve y práctico sobre cómo vestirse hoy."
        )
 
        print("\nGenerando consejo de vestimenta con IA...")
        respuesta = model.generate_content(prompt)
        print("\n--- CONSEJO IA ---")
        print(respuesta.text)
 
    except Exception as e:
        print("Error al conectar con Gemini:", e)
 
# -------------------------
# MENÚS
# -------------------------
 
def menu_acceso():
    while True:
        print("\n--- GUARDIÁNCLIMA ITBA ---")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Salir")
 
        opcion = input("Seleccioná una opción: ")
 
        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                return usuario
        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                return usuario
        elif opcion == "3":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción inválida.")
 
def menu_principal(usuario):
    ultima_consulta = None
 
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Consultar clima y guardar en historial")
        print("2. Ver mi historial por ciudad")
        print("3. Ver estadísticas globales")
        print("4. Consejo IA: ¿Cómo me visto hoy?")
        print("5. Cerrar sesión")
 
        opcion = input("Seleccioná una opción: ")
 
        if opcion == "1":
            ciudad = input("Ingresá el nombre de la ciudad: ")
            datos = consultar_clima(ciudad)
            if datos:
                guardar_historial(usuario, datos)
                ultima_consulta = datos
        elif opcion == "2":
            ver_historial(usuario)
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            if ultima_consulta:
                consejo_vestimenta(ultima_consulta)
            else:
                print("Primero consultá el clima (opción 1).")
        elif opcion == "5":
            print("Cerrando sesión...")
            return
        else:
            print("Opción inválida.")
 
# -------------------------
# INICIO DEL PROGRAMA
# -------------------------
 
verificar_archivos()
 
while True:
    usuario_activo = menu_acceso()
    menu_principal(usuario_activo)