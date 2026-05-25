# Sistema de Gastos Personales

Trabajo grupal desarrollado para la Challenge de Tecnología.

## ¿Qué hace la aplicación?
Un sistema de gestión de gastos personales por consola que permite a múltiples usuarios registrar, visualizar y analizar sus gastos de forma segura.

## Funcionalidades
- Login con usuario y contraseña
- Registro de gastos en archivo CSV
- Visualización de gastos por usuario
- Estadísticas (total, promedio, máximo y mínimo)
- Gráfico de barras por categoría
- Recomendaciones automáticas basadas en los gastos

## Tecnologías utilizadas
- Python
- CSV para almacenamiento de datos
- Matplotlib para visualización de gráficos
- GitHub para trabajo colaborativo

## ¿Cómo correrlo?
1. Tener Python instalado
2. Instalar matplotlib: `pip install matplotlib` (en la consola)
3. Correr el archivo `Trabajo-tec.py`

## Usuarios disponibles
Por defecto el sistema tiene dos usuarios creados:
- Usuario: Alexis | Contraseña: 4044
- Usuario: Maria | Contraseña: 5678

Para agregar nuevos usuarios simplemente modificá el diccionario "usuarios" al inicio del código.

##¿Cómo borrar el historial de gastos?
Simplemente borrá el archivo `gastos.csv` de la carpeta del proyecto. La próxima vez que corras el programa lo crea vacío automáticamente.
