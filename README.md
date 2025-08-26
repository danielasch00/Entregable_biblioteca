# Sistema de Gestión de Biblioteca (Python)

Aplicación de consola para gestionar **libros**, **usuarios** y **préstamos**.  
Permite *agregar*, *buscar*, *listar* y *eliminar*; además de *prestar*, *devolver* y *listar préstamos*.  
Las búsquedas son **exactas normalizadas** (se comparan en minúsculas y sin espacios extra al principio o al final).

---

## Contenidos
- [Requisitos](#requisitos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Cómo ejecutar](#cómo-ejecutar)
- [Qué hace cada opción](#qué-hace-cada-opción)
  - [Menú principal](#menú-principal)
  - [Submenú: Buscar libro](#submenú-buscar-libro)
  - [Submenú: Préstamos](#submenú-préstamos)
  - [Submenú: Buscar usuario](#submenú-buscar-usuario)
- [Datos de ejemplo](#datos-de-ejemplo)
- [Decisiones de diseño](#decisiones-de-diseño)
- [Limitaciones y mejoras](#limitaciones-y-mejoras)
- [Solución de problemas](#solución-de-problemas)

---

## Requisitos
- **Python 3.x** (sin librerías externas).

---

## Estructura del proyecto
```
Entregable_biblioteca/
└─ src/
   ├─ main.py
   ├─ biblioteca.py
   ├─ libro.py
   ├─ usuario.py
   └─ prestamo.py
```

- `main.py`: interfaz por consola y carga de datos de ejemplo.
- `biblioteca.py`: lógica de negocio (altas/bajas/búsquedas, prestar/devolver, listar préstamos).
- `libro.py`: clase `Libro`.
- `usuario.py`: clase `Usuario`.
- `prestamo.py`: clase `Prestamo`.

---

## Cómo ejecutar

### Windows (PowerShell o CMD)
```bash
cd src
python main.py
```

### macOS / Linux
```bash
cd src
python3 main.py
```

---

## Qué hace cada opción

### Menú principal
1. **Agregar libro**  
   Carga *título*, *autor*, *editorial*, *año* y *cantidad*.  
   *Año* y *cantidad* se validan como enteros (si no son números, pide reingresar).

2. **Eliminar libro**  
   Borra un libro por **título** (coincidencia exacta normalizada).  
   Si existen **préstamos activos** de ese título, **bloquea** la eliminación.

3. **Listar libros**  
   Muestra todos los libros en formato breve.

4. **Buscar libro**  
   Abre el submenú para buscar por **título**, **autor** o **editorial** (coincidencia exacta normalizada).

5. **Sección préstamos**  
   Abre opciones de **usuarios**, **préstamos** y **devoluciones**.

6. **Salir**  
   Cierra la aplicación.

---

### Submenú: Buscar libro
1. **Por título** — coincidencia **exacta normalizada** del título.  
2. **Por autor** — coincidencia **exacta normalizada** del autor.  
3. **Por editorial** — coincidencia **exacta normalizada** de la editorial.  
4. **Volver** — regresa al menú anterior.  
5. **Salir** — cierra la aplicación.

---

### Submenú: Préstamos
1. **Registrar usuario**  
   Alta de usuario con *nombre*, *apellido*, *DNI*, *dirección* y *teléfono*.

2. **Eliminar usuario**  
   Elimina por **DNI**. Si el usuario tiene **préstamos activos**, **no** se puede eliminar.

3. **Listar usuarios**  
   Muestra todos los usuarios registrados.

4. **Buscar usuario**  
   Abre el submenú para buscar por **nombre**, **apellido** o **DNI**.

5. **Prestar libro**  
   Pide **DNI** y **título**. Si el usuario existe y hay stock, crea el préstamo, descuenta un ejemplar y lo agrega a las listas correspondientes.

6. **Devolución libro**  
   Pide **DNI** y **título**. Revierte el préstamo: suma el ejemplar al stock y limpia las listas.

7. **Listar préstamos**  
   Muestra los **préstamos vigentes** (usuario → título).

8. **Volver**  
   Regresa al menú anterior.

9. **Salir**  
   Cierra la aplicación.

---

### Submenú: Buscar usuario
1. **Por nombre** — coincidencia **exacta normalizada** del nombre.  
2. **Por apellido** — coincidencia **exacta normalizada** del apellido.  
3. **Por DNI** — comparación **exacta** (se ignoran espacios alrededor).  
4. **Volver** — regresa al menú anterior.  
5. **Salir** — cierra la aplicación.

---

## Datos de ejemplo
Al iniciar, se cargan **5 libros** y **5 usuarios** para probar búsquedas, préstamos, devoluciones y bloqueos de eliminación.  
Esto se hace en `seed_demo_data` dentro de `main.py`.

---

## Decisiones de diseño
- **Búsquedas exactas normalizadas**: se comparan textos *en minúsculas* y *sin espacios extra* al principio/fin.  
- **DNI**: se trata como **texto** y se compara exacto con `strip()` (tolerando espacios alrededor).  
- **Integridad**:
  - No se elimina un **libro** con préstamos activos de ese título.
  - No se elimina un **usuario** con préstamos activos.

---

## Solución de problemas
- **No se elimina un libro/usuario**  
  Revisá si hay **préstamos activos**. Devolvé primero y luego eliminá.

- **No toma año/cantidad**  
  Esos campos deben ser **enteros**. Si no lo son, el programa te lo va a pedir de nuevo.
