# Sistema de Gestión de Tareas con API REST

## Descripción

Este proyecto implementa una API REST desarrollada con Python y Flask.

El sistema permite:

- Registrar usuarios
- Iniciar sesión
- Consultar una página de bienvenida del sistema de tareas

Los datos se almacenan de forma persistente utilizando SQLite, y las contraseñas se almacenan protegidas mediante hash.

---

## Tecnologías utilizadas

- Python 3
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- Werkzeug Security

---

## Instalación

Instalar dependencias:

```bash
pip install flask werkzeug
```

---

## Ejecución

Ejecutar el servidor:

```bash
python servidor.py
```

Servidor disponible en:

```text
http://127.0.0.1:5000
```

---

## Endpoints

### Registro de usuarios

**POST** `/registro`

Body JSON:

```json
{
  "user": "admin",
  "password": "1234"
}
```

---

### Inicio de sesión

**POST** `/login`

Body JSON:

```json
{
  "user": "admin",
  "password": "1234"
}
```

---

### Sistema de tareas

**GET** `/tareas`

Muestra una página HTML de bienvenida.

---

## Seguridad

Las contraseñas no se almacenan en texto plano.

Se utiliza hash para proteger la información sensible de los usuarios.

---

## Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Hashear contraseñas permite proteger información sensible.  
Si una base de datos es comprometida, las contraseñas reales no quedan expuestas.

---

### Ventajas de usar SQLite

SQLite es una buena opción para este proyecto porque:

- No requiere instalar un servidor externo.
- Es liviano y fácil de integrar con Python.
- Permite persistencia local de datos.
- Es ideal para proyectos académicos y prototipos.
