# Sistema de Gestión de Paquetes

## Tabla de Contenido
- [Descripción](#descripción)
- [Características principales](#características-principales)
- [Tipos de Usuarios](#tipos-de-usuarios)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Seguridad](#seguridad)
- [Arquitectura](#arquitectura)
- [API](#api)
- [Contribución](#contribución)
- [Equipo](#equipo)
- [Licencia](#licencia)
## Descripción
El **Sistema de Gestión de Paquetes** es una aplicación diseñada para optimizar y modernizar la administración de envíos y paquetes en empresas logísticas. Este software proporciona herramientas avanzadas para la gestión integral de envíos, rastreo de paquetes, autenticación de usuarios, facturación automatizada y pagos electrónicos, mejorando la eficiencia operativa y la experiencia del cliente.

## Características principales
- **Gestión de paquetes:** Creación, actualización, eliminación y clasificación de paquetes.
- **Gestión de envíos:** Administración y rastreo en tiempo real de paquetes.
- **Gestión de usuarios:** Diferentes roles con niveles de acceso diferenciados.
- **Gestión de pagos y facturación:** Facturación automática y procesamientos de pagos en línea.
- **Búsqueda avanzada:** Filtrado de paquetes según criterios específicos.
## Tipos de Usuarios
- **Cliente:** Puede crear, rastrear y pagar envíos.
- **Administrador:** Supervisa y gestiona todas las funcionalidades.
- **Encargado de envíos:** Responsable de la entrega y actualización del estado de los paquetes.

## Tecnologías Utilizadas
- **Lenguajes y Frameworks:** Python 3.9
- **Base de Datos:** Oracle Database.
- **Herramientas de Desarrollo:**- Docker, Git, GitHub Actions.
- **Pagos:** Integración con PSE para transacciones seguras.

## Instalación y Configuración
1. Clona este repositorio:
2. Crear y activar el entorno virtual:

**Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Instalar las dependencias necesarias
```bash
pip install -r requirements.txt
```
## Seguridad
- **Cifrado de datos sensibles.**
- **Control de acceso basado en roles.**
- **Conexiones seguras para protección de información.**
## Arquitectura
```
SGPAQUETES
├── .github/workflows/
│   ├── ci.yml
│   ├── sonarcloud.yml
├── Docs/
│   ├── Directions.pdf
│   ├── Requerimientos Sistema Gestión.pdf
│   ├── UTB_Template (2).pdf
│   ├── prueba.txt
├── source/
│   ├── __pycache__/
│   │   ├── creation_a.cpython-312.pyc
│   │   ├── excel_creation.cpython-312.pyc
│   │   ├── management_e.cpython-312.pyc
│   │   ├── management_p.cpython-312.pyc
│   │   ├── menu_u.cpython-312.pyc
│   │   ├── users_p.cpython-313.pyc
│   │   ├── users_packages.cpython-312.pyc
│   ├── __init__.py
│   ├── creation_a.py
│   ├── excel_creation.py
│   ├── main.py
│   ├── management_e.py
│   ├── management_p.py
│   ├── menu_u.py
│   ├── users_packages.py
├── tests/
│   ├── tests/
│   │   ├── test_sample.py
│   │   ├── __init__.py
│   ├── prueba.py
│   ├── test_sample.py
├── LICENSE
├── README.md
├── dockerfile
├── packages.xlsx
├── requirements.txt
├── sonar-project.properties
├── users.txt
```
## API
## Gestion de usuario (users_packeges)

### `hash_password(password: str) -> str`
Cifra una contraseña usando SHA-256.

### `input_user_data() -> tuple`
Solicita y retorna el nombre de usuario y la contraseña.

### `register_user() -> None`
Registra un nuevo usuario y almacena su información.

### `authenticate_user() -> None`
Verifica credenciales y redirige al menú según el tipo de usuario.

### `update_d(cls, user: str) -> None`
Permite modificar detalles de los paquetes en un archivo de Excel.

### `menu_customer(user) -> None`  
Muestra el menú para clientes, permitiéndoles gestionar productos, realizar pedidos y ver su estado.  

## Gestión de Paquetes

### `save(cls, package) -> None`  
Guarda la información de un paquete en un archivo de Excel.  

### `show(cls) -> None`  
Muestra la lista de paquetes almacenados en un archivo de Excel.  

### `show_dis(cls) -> None`  
Muestra los paquetes pendientes de entrega en un archivo de Excel.  

### `place_order(usuario) -> None`  
Permite a un usuario realizar un pedido seleccionando un paquete disponible.  

### `update_d(cls, user) -> None`  
Permite a un usuario modificar la información de sus paquetes almacenados en un archivo de Excel.  

### `__init__(self, name, weight, price, type, content=None, category=None, dimension=None, order_status=None, address=None, domiciliary=None)`  
Inicializa un objeto de paquete con sus atributos principales.  

### `__str__() -> str`  
Devuelve una representación en texto del paquete con sus detalles.  

---

## Menús

### `menu() -> None`  
Muestra el menú principal, permitiendo registrar usuarios, iniciar sesión o salir.  

### `menu_customer(user) -> None`  
Muestra el menú para clientes, permitiéndoles gestionar productos, realizar pedidos y ver su estado.  

### `menu_administrator(user) -> None`  
Muestra el menú para administradores, permitiéndoles agregar productos, ver pedidos y gestionar usuarios.  

### `menu_domiciliary(user) -> None`  
Muestra el menú para domiciliarios, permitiéndoles ver y actualizar el estado de los pedidos.  
