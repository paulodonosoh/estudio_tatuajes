# estudio_tatuajes
en este proyecto se desarrollara una aplicacion web que permita gestionar y dar a conocer los servicion de un estudio de tatuajes que trabaja con varios tatuadores
se pretende implementar funcionalidades de gestios de reservas de cupos y exposicion del trabajo y especialidades de los artista mediante galerias con trabajos previos de los artistas
el objetivo final de este proyecto es que la aplicacion permita gestionar un estudio de tatuajes en su totalidad, como promocionar a los artistas y exponer su trabajo, dar a conocer los distintos tipos de especialidades de tatuajes que existen y estan disponibles en el estudio, gestion de reservas, administracion de personal y horarios de artistas por parte de un administrador

# Estudio de Tatuajes - Módulo Galería y Gestión (CRUD)

Este es mi proyecto de aplicación web desarrollada con Django para un estudio de tatuajes. Para esta entrega (Rúbrica 2), implementé un sistema de persistencia de datos y un CRUD completo que me permite administrar el portafolio de trabajos y bocetos desde la propia interfaz web.

## 🚀 Características que implementé

* **Base de Datos (PostgreSQL):** Conecté el proyecto a una base de datos relacional para dejar de usar datos estáticos.
* **Seguridad:** Usé la librería `python-dotenv` para proteger mis credenciales locales mediante un archivo `.env` que no se sube a GitHub.
* **CRUD Completo:** Creé las vistas, rutas y plantillas para poder Añadir, Leer, Editar y Eliminar tatuajes directamente desde el navegador.
* **Filtro de Pestañas:** Agregué una columna booleana (`es_disponible`) en mi modelo para que la galería separe automáticamente los "Trabajos Realizados" de los "Diseños Disponibles" (bocetos).
* **Validación de Formularios:** Configuré un `ModelForm` con validaciones propias para asegurar que los datos ingresados sean correctos.
* **Git Flow:** Trabajé todo el desarrollo separando el proyecto por ramas (`feature/bd-y-modelos`, `feature/vistas-crud`, etc.) para mantener mi historial ordenado.

## ⚙️ Cómo levantar mi proyecto localmente

Si necesitas probar mi proyecto, sigue estos pasos:

1. **Clonar el repositorio e instalar dependencias:**
   Clona mi repositorio, entra a la carpeta, crea tu entorno virtual e instala los requerimientos:
   ```bash
   pip install -r requirements.txt

   Configurar la Base de Datos:
Crea una base de datos vacía en tu pgAdmin llamada estudio_tatuajes_db. Luego, crea un archivo .env en la raíz de este proyecto con tus credenciales:

Fragmento de código
DB_NAME=estudio_tatuajes_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aqui
DB_HOST=localhost
DB_PORT=5432

2. **Ejecutar migraciones y levantar el servidor:**

Bash
python manage.py migrate
python manage.py runserver
Mi proyecto estará corriendo en http://127.0.0.1:8000/.

## App Reserva - Funcionalidades implementadas

La aplicación `reserva` ya cuenta con las siguientes funcionalidades:

* **CRUD completo de reservas:** permite crear, listar, editar y eliminar reservas desde la interfaz web.
* **Asociación con artistas:** cada reserva queda vinculada a un artista específico del estudio.
* **Validación de horarios:** se controla que la hora de término sea mayor que la de inicio y se evita crear reservas inconsistentes.
* **Calendario semanal:** muestra la disponibilidad por día y horario con base en las reservas registradas en la base de datos.
* **Filtro por artista:** el calendario puede visualizarse por artista para consultar su disponibilidad individual.
* **Estados de reserva:** las reservas pueden registrarse con estados como pendiente o confirmada.
* **Navegación por semanas:** el calendario permite avanzar o retroceder por semanas futuras/pasadas para revisar disponibilidad.
* **Formularios con validación:** el `ModelForm` valida los datos antes de guardar la reserva, asegurando integridad en la información.