# Blockchain Viewer PRO

**Blockchain Viewer PRO** es una aplicación de escritorio avanzada, desarrollada en Python y PyQt5, que permite la visualización y el análisis en tiempo real de las transacciones de la red Bitcoin. Este proyecto está diseñado para ser una herramienta potente y educativa, ideal para entusiastas de las criptomonedas, analistas de datos y desarrolladores que deseen explorar el fascinante mundo de la blockchain.

---

## Características Principales

- **Visualización en Tiempo Real**: Observa el flujo constante de transacciones de Bitcoin a medida que se producen, con actualizaciones automáticas cada pocos segundos.
- **Filtrado Avanzado**: Personaliza la visualización de datos con filtros inteligentes para identificar transacciones de interés, como:
  - **Ballenas**: Transacciones de alto valor que pueden indicar movimientos importantes en el mercado.
  - **Fee Bajo**: Transacciones con comisiones inusualmente bajas.
  - **Mixers**: Detección de transacciones que podrían estar utilizando servicios de mezcla para ofuscar su origen (funcionalidad en desarrollo).
- **Exportación de Datos**: Guarda los datos de las transacciones filtradas en formato CSV con un solo clic, facilitando su análisis posterior en otras herramientas.
- **Interfaz de Usuario Moderna**: Una interfaz gráfica limpia, intuitiva y fácil de usar, desarrollada con PyQt5 para una experiencia de usuario fluida.
- **Código Modular y Extensible**: La arquitectura del proyecto está diseñada para ser fácil de entender, mantener y ampliar, con una clara separación entre la lógica de la aplicación y la interfaz de usuario.

---

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.10+
- **Interfaz Gráfica**: PyQt5
- **Comunicaciones**: `requests` para la interacción con la API de mempool.space.
- **Manejo de Datos**: Módulos `csv` y `datetime` para la exportación y gestión de datos.

---

## Instalación y Ejecución

Sigue estos pasos para poner en marcha la aplicación en tu sistema local.

### Requisitos Previos

- Python 3.10 o superior.
- `pip` (el gestor de paquetes de Python).
- Acceso a Internet.

### Pasos de Instalación

1.  **Clona el repositorio**:
    ```bash
    git clone https://github.com/quantumvortex369/BlockchainViewerPro.git
    cd BlockchainViewerPro
    ```

2.  **Crea y activa un entorno virtual** (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *En Windows, usa `venv\Scripts\activate`*

3.  **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación**:
    ```bash
    python main.py
    ```

---

## Cómo Usar la Aplicación

1.  **Pantalla de Inicio**: Al ejecutar la aplicación, serás recibido por una pantalla de bienvenida. Haz clic en **"Iniciar"** para acceder al visualizador de transacciones.
2.  **Visualizador de Transacciones**: Una vez dentro, la aplicación comenzará a mostrar las transacciones más recientes de la red Bitcoin en tiempo real.
3.  **Aplicar Filtros**: En la parte superior, encontrarás varias casillas de verificación para filtrar las transacciones. Puedes seleccionar "Ballenas", "Fee Bajo" o "Mixers". Si seleccionas "Todas", se mostrarán todas las transacciones sin filtrar.
4.  **Control de la Visualización**: Usa los botones **"Empezar"** y **"Apagar"** para iniciar o detener la actualización en tiempo real de las transacciones.
5.  **Exportar a CSV**: Haz clic en el botón **"Exportar CSV"** para guardar los datos que se están mostrando actualmente en la tabla en un archivo `.csv` en tu disco local.

---

## Estructura del Proyecto

El código fuente está organizado de la siguiente manera para facilitar su comprensión y mantenimiento:

```
BlockchainViewerPro/
├── api/
│   └── mempool.py      # Lógica para la comunicación con la API de mempool.space
├── ui/
│   ├── __init__.py
│   ├── inicio_app.py   # Código de la pantalla de inicio
│   └── blockchain_viewer.py # Código de la pantalla principal del visualizador
├── utils/
│   └── exporter.py     # Lógica para la exportación de datos a CSV
├── venv/                 # Entorno virtual (si se crea)
├── constants.py          # Constantes de la aplicación
├── main.py               # Punto de entrada principal de la aplicación
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## Contribuciones

Este es un proyecto en desarrollo activo y las contribuciones son bienvenidas. Si tienes ideas para nuevas funcionalidades, mejoras en el código o has encontrado un error, no dudes en:

1.  Hacer un **fork** de este repositorio.
2.  Crear una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3.  Realizar tus cambios y hacer **commit**.
4.  Enviar un **Pull Request** para que tus cambios sean revisados.

También puedes abrir un **issue** para reportar errores o proponer nuevas ideas.

---

## Desarrollado por Nexus
