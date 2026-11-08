# estudio_tatuajes
en este proyecto se desarrollara una aplicacion web que permita gestionar y dar a conocer los servicion de un estudio de tatuajes que trabaja con varios tatuadores
se pretende implementar funcionalidades de gestios de reservas de cupos y exposicion del trabajo y especialidades de los artista mediante galerias con trabajos previos de los artistas
el objetivo final de este proyecto es que la aplicacion permita gestionar un estudio de tatuajes en su totalidad, como promocionar a los artistas y exponer su trabajo, dar a conocer los distintos tipos de especialidades de tatuajes que existen y estan disponibles en el estudio, gestion de reservas, administracion de personal y horarios de artistas por parte de un administrador

# Estudio de Tatuajes - Módulo Galería y Gestión (CRUD)

Este es mi proyecto de aplicación web desarrollada con Django para un estudio de tatuajes. Para esta entrega (Rúbrica 2), implementé un sistema de persistencia de datos y un CRUD completo que me permite administrar el portafolio de trabajos y bocetos desde la propia interfaz web.

## Estudio de Tatuajes

Aplicacion web desarrollada con Django para gestionar un estudio de tatuajes con varios artistas. El proyecto permite administrar artistas, galeria de trabajos, cotizaciones y reservas mediante paginas HTML y Django Admin.

La API REST agrega una forma de consumir los mismos datos desde herramientas como Postman o Thunder Client, sin reemplazar la aplicacion web existente.

## Funcionalidades

- Gestion de artistas y sus especialidades.
- Galeria de trabajos realizados y diseños disponibles.
- Cotizador de tatuajes.
- CRUD web de reservas.
- Calendario de disponibilidad por artista.
- API REST de reservas.
- Autenticacion JWT para operaciones de escritura en la API.
- PostgreSQL configurado mediante variables de entorno.

## Requisitos

- Python 3.13 o compatible.
- PostgreSQL.
- Git.

## Instalacion local

1. Clonar el repositorio y entrar en la carpeta del proyecto.

2. Crear y activar el entorno virtual:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Crear una base de datos PostgreSQL, por ejemplo `estudio_tatuajes_db`.

5. Copiar `.env.example` como `.env` y completar los valores locales:

   ```env
   SECRET_KEY=clave-local-de-desarrollo
   DEBUG=True
   DB_NAME=estudio_tatuajes_db
   DB_USER=postgres
   DB_PASSWORD=tu_clave_local
   DB_HOST=localhost
   DB_PORT=5432
   ```

   El archivo `.env` no debe publicarse ni contenerse en capturas del informe. Se debe conservar `.env.example` sin credenciales reales.

6. Ejecutar las migraciones:

   ```powershell
   python manage.py migrate
   ```

7. Levantar el servidor:

   ```powershell
   python manage.py runserver
   ```

   El sitio queda disponible en `http://127.0.0.1:8000/`.

## Aplicaciones Django

- `core`: paginas principales del sitio.
- `artistas`: gestion de tatuadores y sus datos.
- `reserva`: reservas, calendario y API REST.
- `galeria`: trabajos y diseños disponibles.
- `cotizador`: calculadora de precios estimados.

## API REST de reservas

La API utiliza Django REST Framework y `djangorestframework-simplejwt`. El recurso principal es `Reserva`, que se conecta con el modelo existente `Artista`.

### Autenticacion JWT

Obtener tokens:

```http
POST /api/token/
```

Body JSON:

```json
{
  "username": "api_demo",
   "password": "TU_CONTRASENA_LOCAL"
}
```

La respuesta contiene los tokens `access` y `refresh`. Para renovar el access token:

```http
POST /api/token/refresh/
```

Body JSON:

```json
{
  "refresh": "tu_refresh_token"
}
```

Las operaciones protegidas deben enviar el access token en el encabezado:

```http
Authorization: Bearer tu_access_token
```

El usuario `api_demo` es solo para pruebas locales. La contraseña debe configurarse localmente y no debe publicarse en el repositorio, capturas o informe.

### Endpoints

| Metodo | Ruta | Proteccion | Proposito |
| --- | --- | --- | --- |
| GET | `/api/reservas/` | Publica | Listar reservas |
| GET | `/api/reservas/<id>/` | Publica | Consultar una reserva |
| POST | `/api/reservas/` | JWT obligatorio | Crear una reserva |
| PATCH | `/api/reservas/<id>/` | JWT obligatorio | Modificar parcialmente una reserva |
| PUT | `/api/reservas/<id>/` | JWT obligatorio | Reemplazar una reserva |
| DELETE | `/api/reservas/<id>/` | JWT obligatorio | Eliminar una reserva |

### Crear una reserva

```http
POST /api/reservas/
```

Body de ejemplo:

```json
{
  "nombre_cliente": "Cliente API",
  "telefono": "56912345678",
  "email": "cliente@example.com",
  "artista": 1,
  "fecha": "2026-11-10",
  "hora_inicio": "10:00:00",
  "hora_fin": "11:00:00",
  "descripcion": "Reserva creada mediante la API"
}
```

El campo `artista` debe corresponder al ID de un artista existente. El campo `estado` es opcional y utiliza `pendiente` por defecto.

### Validaciones

- Los campos obligatorios no pueden estar vacios.
- La fecha no puede estar en el pasado.
- `hora_fin` debe ser posterior a `hora_inicio`.
- El artista debe existir.
- `estado` solo acepta los valores definidos por el modelo.
- `id`, `creado_en` y `actualizado_en` son campos de solo lectura.

### Respuestas esperadas

- `200 OK`: consulta o modificacion exitosa.
- `201 Created`: reserva creada.
- `204 No Content`: reserva eliminada.
- `400 Bad Request`: datos invalidos.
- `401 Unauthorized`: falta el token o esta expirado.
- `404 Not Found`: la reserva no existe.

## Pruebas

La API fue probada con Django REST Framework y puede verificarse con Postman o Thunder Client en este orden:

1. Obtener `access` y `refresh` en `/api/token/`.
2. Renovar el access token en `/api/token/refresh/`.
3. Ejecutar un `GET /api/reservas/` sin token.
4. Crear una reserva con `POST` y Bearer token.
5. Modificarla con `PATCH` y Bearer token.
6. Consultarla mediante su identificador.
7. Eliminarla con `DELETE` y Bearer token.
8. Repetir un `POST` sin token y comprobar el `401`.
9. Enviar una fecha pasada u horarios invalidos y comprobar el `400`.

Para ejecutar las pruebas automatizadas:

```powershell
python manage.py test
```

Las pruebas incluyen autenticacion JWT, permisos, CRUD y validaciones de fecha y horario.

## Seguridad y variables de entorno

- No publicar `.env`.
- No incluir contraseñas reales en el README, capturas o commits.
- Mantener `.env.example` con valores de ejemplo.
- Usar tokens de prueba solo durante el desarrollo.
- Renovar el access token cuando expire; no enviar el refresh token a endpoints CRUD.

## Continuidad del proyecto

La API utiliza los modelos y la base de datos PostgreSQL del proyecto original. Las paginas HTML, Django Admin y las aplicaciones existentes siguen funcionando junto con los nuevos endpoints REST.