# Blockchain Viewer PRO

**Blockchain Viewer PRO** es una aplicación de escritorio desarrollada en Python utilizando la librería PyQt5, diseñada para visualizar en tiempo real las transacciones que ocurren en la red Bitcoin. Este proyecto combina análisis de datos en vivo, filtrado inteligente y una interfaz gráfica moderna, orientada tanto a curiosos como a analistas y desarrolladores del mundo cripto.

---

## Características principales

- **Visualización en tiempo real:** Accede al flujo de transacciones conforme se propagan en la red Bitcoin.
- **Filtrado avanzado:** Elige visualizar solo transacciones específicas según criterios como:
  - Alto valor (ballenas)
  - Transacciones a mixers
  - Comisiones anormalmente bajas
- **Exportación de datos:** Guarda información relevante en archivos CSV para su posterior análisis.
- **Interfaz intuitiva:** Desarrollada con PyQt5, ofrece una experiencia fluida y accesible.
- **Modularidad y extensibilidad:** Código limpio y estructurado para facilitar la comprensión, modificación y ampliación.

---

## Tecnologías utilizadas

- **Python 3.10+**
- **PyQt5** – Interfaz gráfica
- **requests** – Conexión con APIs blockchain
- **csv / os / json** – Manipulación de datos
- **threading / multiprocessing** – Optimización del rendimiento y fluidez de la GUI

---

## Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener:

- Python 3.10 o superior instalado
- pip actualizado
- Acceso a internet (para conexión a nodos o APIs públicas de blockchain)

---

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/quantumvortex369/BlockchainViewerPro.git
```
```bash
cd BlockchainViewerPro
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python blockchainviewerpro.py
```

## Casos de uso
- Monitoreo de ballenas y flujos grandes de BTC

- Educación y demostración en tiempo real de cómo funciona la red Bitcoin

- Benchmark de fees y congestión de red

---

## ¿Para quién está pensado?
- Desarrolladores que buscan inspiración o base para apps reales en PyQt5

- Analistas on-chain que desean herramientas visuales para entender el flujo económico de la red

- Hackers éticos y ciberentusiastas que experimentan con tecnologías descentralizadas

- Estudiantes y autodidactas que quieren entender Bitcoin desde dentro

---

## Contribuciones
Este proyecto está en desarrollo activo. Si tienes sugerencias, mejoras o deseas colaborar:

- Haz un fork del repositorio

- Crea tu rama con git checkout -b feature/nueva-funcionalidad

- Realiza tus cambios y haz commit

- Abre un Pull Request

- También puedes abrir issues para reportar bugs o proponer ideas.

---

## Desarrollado por Nexus
