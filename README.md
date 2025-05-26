# PaymentManager Backend

Sistema de gestión de pagos y domiciliaciones bancarias desarrollado en Django REST Framework, diseñado para procesar y administrar cobros automáticos entre diferentes instituciones bancarias mexicanas.

## Arquitectura del Sistema

![Imagen de WhatsApp 2025-05-25 a las 11 47 46_24a5abf3](https://github.com/user-attachments/assets/a610a70a-4777-478d-bfa2-4d89b1c17f9f)

### Stack Tecnológico

- **Framework Backend**: Django 5.2.1 + Django REST Framework 3.16.0
- **Autenticación**: JWT (JSON Web Tokens) con Simple JWT
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Lenguaje**: Python 3.x
- **Gestión de Variables**: python-dotenv para configuración de entorno

### Estructura del Proyecto

```
PaymentManager/
├── PaymentManager/           # Configuración principal del proyecto
│   ├── settings.py          # Configuraciones Django
│   ├── urls.py              # Routing principal
│   ├── wsgi.py              # Interfaz WSGI
│   └── asgi.py              # Interfaz ASGI
├── apps/                    # Aplicaciones Django
│   ├── AuthSystem/          # Sistema de autenticación
│   └── MagicTool/           # Módulo de gestión de pagos
├── .env                     # Variables de entorno
├── manage.py                # Comando Django
└── requirements.txt         # Dependencias Python
```

## Módulos del Sistema

### 1. AuthSystem (Sistema de Autenticación)

Sistema completo de gestión de usuarios con autenticación JWT, que incluye:

#### Características
- **Modelo de Usuario Personalizado**: Extiende AbstractUser con email como identificador único
- **Autenticación JWT**: Tokens de acceso y refresh con rotación automática
- **Gestión de Sesiones**: Login, logout con blacklist de tokens
- **Administración de Usuarios**: Registro, actualización de perfil, cambio de contraseñas

#### Endpoints Principales
```
POST /api/auth/login/              # Autenticación de usuario
POST /api/auth/register/           # Registro de nuevo usuario
GET  /api/auth/profile/            # Obtener perfil del usuario autenticado
PUT  /api/auth/profile/update/     # Actualizar perfil
POST /api/auth/change-password/    # Cambiar contraseña
POST /api/auth/logout/             # Cerrar sesión
GET  /api/auth/verify-token/       # Verificar validez del token
GET  /api/auth/users/              # Listar usuarios (solo admin)
```

#### Configuración JWT
- **Access Token**: 60 minutos de vigencia
- **Refresh Token**: 7 días de vigencia con rotación automática
- **Blacklist**: Los tokens se invalidan automáticamente al cerrar sesión

### 2. MagicTool (Gestión de Pagos)

Módulo central para el procesamiento de domiciliaciones bancarias y gestión de cobros.

#### Modelos de Datos

**RespuestaBanco**: Catálogo de códigos de respuesta bancaria (>100 códigos diferentes)
- Respuestas exitosas: 'DOM1', 'INC0', etc.
- Errores de cuenta: Inexistente, bloqueada, cancelada, fondos insuficientes
- Errores de proceso: Duplicados, fuera de horario, datos inválidos

**Banco**: Catálogo de instituciones financieras mexicanas
- Bancos principales: BBVA, Santander, Banamex, HSBC, Banorte
- Instituciones especializadas: NAFIN, BANOBRAS, STP
- Casas de bolsa y cambio

**Credito**: Registro de créditos del sistema
- Identificador único por crédito

**Emisora**: Configuración de emisores de domiciliación
- Asociación banco-emisora
- Tipos de envío: TRADICIONAL, CUENTA, TARJETA, INTERBANCARIO, etc.

**ListaCobro**: Listas de cobro organizadas
- Agrupación por banco, fecha y emisora
- Control de horarios de procesamiento

**Cobro**: Transacciones individuales de cobro
- Montos: exigible, a cobrar, cobrado
- Referencias: crédito, banco, respuesta, lista
- Trazabilidad completa de la transacción

**Logs**: Sistema de auditoría
- Registro timestamped de eventos
- Niveles de logging
- Resultados de operaciones

#### Endpoints API
Cada modelo cuenta con endpoints CRUD completos:
```
GET    /api/magic-tool/{modelo}/     # Listar registros
POST   /api/magic-tool/{modelo}/     # Crear registro
GET    /api/magic-tool/{modelo}/{id}/ # Obtener registro específico
PUT    /api/magic-tool/{modelo}/{id}/ # Actualizar registro
DELETE /api/magic-tool/{modelo}/{id}/ # Eliminar registro
```

## Configuración e Instalación

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes Python)
- PostgreSQL (para producción)

### Instalación Local

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd PaymentManager
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
Crear archivo `.env` en la raíz del proyecto:
```env
DB_NAME=credifiel
DB_USER=django_user
DB_PASSWORD=your_password
SECRET_KEY=your-secret-key-here
DEBUG=True
```

5. **Ejecutar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

### Configuración de Base de Datos

#### Desarrollo (SQLite)
Por defecto, el sistema usa SQLite para desarrollo local. No requiere configuración adicional.

#### Producción (PostgreSQL)
Para usar PostgreSQL, descomentar la configuración en `settings.py` y configurar las variables de entorno correspondientes:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

## Importación de Datos

### Comando de Gestión Django
El sistema incluye un comando personalizado para importar cobros desde archivos CSV:

```bash
python manage.py importar_creditos archivo.csv
```

#### Formato del CSV
El archivo CSV debe contener las siguientes columnas:
- `idCredito`: Identificador del crédito
- `montoExigible`: Monto total exigible
- `montoCobrar`: Monto a cobrar en esta transacción
- `montoCobrado`: Monto efectivamente cobrado
- `idRespuestaBanco`: Código de respuesta del banco
- `idBanco`: Identificador del banco
- `idListaCobro`: Identificador de la lista de cobro

### Script de Carga Masiva
Alternativamente, existe un script `load_data.py` para cargas masivas con manejo de errores:

```python
# Modificar la ruta del archivo en load_data.py
archivo = "resources/tu_archivo.csv"
```

## Seguridad

### Autenticación y Autorización
- **JWT Security**: Tokens firmados con HS256
- **Permission Classes**: Todos los endpoints requieren autenticación
- **Token Rotation**: Los refresh tokens se rotan automáticamente
- **Blacklisting**: Invalidación segura de tokens al logout

### Configuraciones de Seguridad
- **CORS**: Configurado para desarrollo (ajustar para producción)
- **DEBUG**: Deshabilitado en producción
- **SECRET_KEY**: Gestionado por variables de entorno
- **Password Validation**: Validadores Django habilitados

## API Documentation

### Autenticación
Todas las peticiones (excepto login y registro) requieren header de autorización:
```
Authorization: Bearer <access_token>
```

### Formato de Respuesta
Las respuestas siguen un formato JSON consistente:
```json
{
    "message": "Mensaje descriptivo",
    "data": { ... },
    "errors": { ... }
}
```

### Paginación
Los endpoints de listado incluyen paginación automática:
- **PAGE_SIZE**: 10 registros por página
- **Navegación**: URLs next/previous en la respuesta

## Desarrollo y Mantenimiento

### Estructura de Aplicaciones Django
El proyecto sigue la arquitectura de aplicaciones separadas:
- **Separación de responsabilidades**: AuthSystem vs MagicTool
- **Modularidad**: Cada app maneja su dominio específico
- **Reutilización**: Componentes independientes y reutilizables

### Best Practices Implementadas
- **Settings por Entorno**: Configuración mediante variables de entorno
- **Serializers Específicos**: Validación y transformación de datos
- **Generic Views**: Uso de vistas genéricas de DRF para consistencia
- **Model Choices**: Catálogos definidos como choices en modelos
- **Logging System**: Registro de eventos para auditoría

### Testing
Los archivos de tests están preparados en cada aplicación:
- `apps/AuthSystem/tests.py`
- `apps/MagicTool/tests.py`

## Localización

El sistema está configurado para México:
- **Idioma**: Español (es-mx)
- **Zona Horaria**: America/Monterrey
- **Monedas**: Configurado para pesos mexicanos

## Consideraciones de Producción

### Variables de Entorno Requeridas
```env
DEBUG=False
SECRET_KEY=<strong-secret-key>
DB_NAME=<database-name>
DB_USER=<database-user>
DB_PASSWORD=<database-password>
DB_HOST=<database-host>
DB_PORT=<database-port>
ALLOWED_HOSTS=<your-domain.com>
```

### Optimizaciones Recomendadas
- Configurar servidor web (Nginx/Apache)
- Implementar cache (Redis/Memcached)
- Configurar logs de aplicación
- Backup automático de base de datos
- Monitoring y alertas

## Soporte y Contribución

Este sistema está diseñado para manejar el flujo completo de domiciliaciones bancarias, desde la creación de listas de cobro hasta el procesamiento de respuestas bancarias, con un enfoque en la trazabilidad, auditoría y seguridad de las transacciones financieras.
