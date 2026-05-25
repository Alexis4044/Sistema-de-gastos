# GuardiánClima ITBA

Trabajo grupal desarrollado para el Challenge Tecnológico del curso introductorio del ITBA.

## ¿Qué hace la aplicación?
GuardiánClima ITBA es un sistema de consola en Python que permite a múltiples usuarios consultar el clima de cualquier ciudad del mundo, guardar un historial de consultas y recibir consejos de vestimenta generados por Inteligencia Artificial.

## Funcionalidades
- Registro de nuevos usuarios con validación de contraseña segura
- Login con usuario y contraseña
- Consulta de clima en tiempo real (temperatura, condición, humedad, viento)
- Historial global de consultas guardado en CSV
- Estadísticas globales (ciudad más consultada, total de consultas, temperatura promedio)
- Consejo de vestimenta generado por IA (Google Gemini)

## Tecnologías utilizadas
- Python 3
- CSV para almacenamiento de usuarios e historial
- API de OpenWeatherMap para datos climáticos
- API de Google Gemini para consejos de IA
- GitHub para trabajo colaborativo

## Instalación de librerías necesarias
Ejecutar en la terminal:
py -m pip install requests google-generativeai

## ¿Cómo correrlo?
1. Tener Python instalado
2. Instalar las librerías (ver arriba)
3. Correr el archivo `guardianclima.py`

## Usuarios
El sistema permite registrar nuevos usuarios directamente desde la aplicación. Las contraseñas deben cumplir con:
- Al menos 8 caracteres
- Al menos una mayúscula
- Al menos un número

## ¿Cómo borrar el historial?
Simplemente borrá el archivo `historial_global.csv` de la carpeta del proyecto. La próxima vez que corras el programa lo crea vacío automáticamente.

## API Keys
El proyecto utiliza dos APIs externas:
- OpenWeatherMap: para consultar el clima en tiempo real
- Google Gemini: para generar consejos de vestimenta con IA

## Desarrolladores
- Alexis
- (nombre compañero)
- (nombre compañero)
