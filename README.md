# Backend Recall

Entrenador de recuperación activa para una entrevista junior de backend con Python, Django y Django REST Framework.

- Django 6.0.8
- 169 ejercicios en 11 módulos
- Todos los ejercicios parten de código, SQL, HTTP o comandos reales
- Modos específicos para debugging, completar código, entrevista y “¿está bien o mal?”
- 20 ejercicios de veredicto: primero se responde y después aparece el motivo
- Interfaz mobile-first con controles táctiles y código adaptado a pantallas chicas
- Sin base de datos requerida en producción
- Progreso guardado en `localStorage`
- API JSON de tarjetas en `/api/cards/`
- Despliegue zero-config en Vercel
- Cada ejercicio enlaza documentación oficial

El hilo conductor es una API de foro con `Post`, `Comentario`, likes y usuarios. El contenido cubre Django, DRF, ORM/PostgreSQL, HTTP, auth/permissions, testing, seguridad, Git/deploy y un repaso corto de Python para backend.

## Local

Requiere Python 3.12+.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

No hace falta ejecutar migraciones: esta versión no usa base de datos.

## Tests

```bash
python manage.py test
```

Los tests validan las páginas/API y también la integridad pedagógica del mazo: IDs únicos, módulos requeridos, fuentes y proporción de ejercicios con código.

## Vercel

Vercel detecta `manage.py` y despliega Django automáticamente.

Configurar en Production:

- `DJANGO_SECRET_KEY`: una clave aleatoria larga.
- Opcional `DJANGO_ALLOWED_HOST`: dominio personalizado, por ejemplo `backendrecall.com`.

El progreso se guarda en el navegador de cada dispositivo. Si más adelante se quiere login/sincronización, conviene agregar Postgres.
