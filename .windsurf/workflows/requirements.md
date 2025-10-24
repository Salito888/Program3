---
description: Desarrollar una API REST con FastAPI para gestionar un Árbol AVL que mantenga balance automático con valores altos, positivos y negativos.
auto_execution_mode: 1
---

# REQUERIMIENTO: API ÁRBOL AVL (BALANCEADO)

## Fase MODEL
### Estructura de NodoAVL
- Atributos:
  - valor id: entero (soporta valores negativos y positivos grandes, este toma la decisión de que lado va a ir el nodo, si a la izquierda o la derecha)
  - nombre del niño: str
  - edad : entero
  - altura: altura del subárbol desde este nodo
  - Balanceo
### Comportamiento del AVL
- Propiedad BST mantenida
- Auto-balanceo mediante rotaciones
- Factor de balance calculado: altura(izquierdo) - altura(derecho)
- Rotaciones aplicadas cuando |factor balance| > 1

### Tipos de Rotaciones
1. *Rotación simple derecha*: caso izquierda-izquierda
2. *Rotación simple izquierda*: caso derecha-derecha
3. *Rotación doble izquierda-derecha*: caso izquierda-derecha
4. *Rotación doble derecha-izquierda*: caso derecha-izquierda

## Fase SERVICE
### Funcionalidades del Servicio AVL
1. *Inserción con auto-balanceo*
   - Inserta manteniendo propiedad BST
   - Actualiza alturas recursivamente
   - Verifica y aplica rotaciones necesarias
   - Acepta mismos valores que ABB para comparación

2. *Verificación de balance AVL*
   - Siempre debe retornar balanceado (true)
   - Verifica que |factor balance| ≤ 1 para todos los nodos

3. *Operaciones de consulta*
   - Recorrido in-order con metadatos AVL
   - Estructura completa con altura y factor de balance
   - Información de rotaciones aplicadas

4. *Ejemplo balanceado*
   - Mismos valores que ABB desbalanceado: [100, -50, 200, -25, 300, -75, 400, -10, 500, -100, 600]
   - Demuestra auto-balanceo automático

### Respuestas del Servicio
- Formato JSON enriquecido con metadatos AVL
- Incluir: altura por nodo, factor de balance, estado de balance
- Estructura jerárquica del árbol

## Fase CONTROLLER
### Endpoints FastAPI
1. *POST /insertar*
   - Body: {"valor": integer}
   - Response: estado AVL después de inserción

2. *GET /estado*
   - Response: estado actual del AVL
   - Incluye: metadatos AVL, balance, estructura

3. *POST /ejemplo-balanceado*
   - Crea AVL balanceado con secuencia específica
   - Response: estado del AVL creado

### Especificaciones Técnicas
- Framework: FastAPI
- Puerto: 8000
- Formato respuestas: JSON con metadatos AVL
- Documentación automática: /docs
- Tipado de datos estricto

## Criterios de Validación
- El árbol debe reportar "balanceado": true siempre
- Debe mantener balance con la misma secuencia que desbalancea al ABB
- Las rotaciones deben aplicarse correctamente
- Metadatos AVL (altura, balance) deben ser precisos
- API debe ser funcional y documentada