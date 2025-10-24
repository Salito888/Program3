
# 🌳 API Árbol AVL — Comandos cURL

Este documento contiene ejemplos de comandos `curl` para interactuar con la API del Árbol AVL.
Reemplaza `http://127.0.0.1:8000` por la URL donde corras tu API.

---

## 📥 Agregar Nodos child (POST /api/v1/child)

### Ejemplo general:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/child" \
     -H "Content-Type: application/json" \
     -d '{"id": 101, "nombre": "María García", "edad": 7}'
```

### Insertar todos los nodos:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":101,"nombre":"María García","edad":7}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":70,"nombre":"Juan Pérez","edad":6}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":6,"nombre":"Ana López","edad":8}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":-2,"nombre":"Carlos Sánchez","edad":7}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":100,"nombre":"Laura Torres","edad":9}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":90,"nombre":"Pedro Ramírez","edad":6}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":30,"nombre":"Sofía Díaz","edad":8}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":46,"nombre":"Diego Castro","edad":7}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":99,"nombre":"Elena Ruiz","edad":9}'
curl -X POST "http://127.0.0.1:8000/api/v1/child" -H "Content-Type: application/json" -d '{"id":33,"nombre":"Miguel Ángel Soto","edad":8}'
```

---

## 📄 Obtener todos los nodos (GET /api/v1/child)

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/child"
```

---

## 🔍 Obtener un nodo por ID (GET /api/v1/child/{id})

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/child/70"
```

---

## 🌲 Ver el árbol completo (GET /api/v1/tree)

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/tree"
```

---

## 🧹 Eliminar todo el árbol (DELETE /api/v1/tree)

```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/tree"
```

---

##  Notas

* Todos los endpoints devuelven respuestas en formato JSON.
* El árbol se balancea automáticamente con cada inserción.
* Si intentas agregar un `id` ya existente, la API devuelve un error `400`.



✅ Autor@: Salomé Granada Henao.
📘 Proyecto: API Árbol AVL
🕓 Versión: 1.0
