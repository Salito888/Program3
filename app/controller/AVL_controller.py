
from fastapi import APIRouter, HTTPException, Request, status, Depends
from typing import Dict, Any, List
import json
import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from service.AVL_service import AVLService

router = APIRouter()

# Inicializar el servicio AVL
avl_service = AVLService()

class ChildData:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

# 1. Endpoint para agregar un niño
@router.post("/child", status_code=status.HTTP_201_CREATED)
async def add_child(request: Request):
    try:
        # Obtener datos del cuerpo de la petición
        body = await request.body()
        data = json.loads(body)
        
        # Validar campos requeridos
        if not all(key in data for key in ["id", "name", "age"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Se requieren los campos: id, name y age"
            )
            
        # Validar tipos de datos
        try:
            child_data = ChildData(
                id=int(data["id"]),
                name=str(data["name"]),
                age=int(data["age"])
            )
        except (ValueError, TypeError):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tipos de datos inválidos. id y age deben ser números, name debe ser texto"
            )
        
        # Insertar en el árbol AVL
        result = avl_service.insert_child(
            id=child_data.id,
            name=child_data.name,
            age=child_data.age
        )
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["message"]
            )
        
        return {
            "status": "success",
            "data": result["child"],
            "message": result["message"],
            "is_balanced": result["is_balanced"]
        }
        
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Formato JSON inválido"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al procesar la solicitud: {str(e)}"
        )

# 2. Endpoint para obtener un niño por ID
@router.get("/child/{child_id}")
async def get_child(child_id: int):
    try:
        result = avl_service.find_child(child_id)
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=result["message"]
            )
            
        return {
            "status": "success",
            "data": result["child"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar el niño: {str(e)}"
        )

# 3. Endpoint para ver el estado del árbol AVL
@router.get("/tree")
async def get_tree():
    try:
        result = avl_service.get_tree()
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result["message"]
            )
            
        return {
            "status": "success",
            "data": result["tree"],
            "is_balanced": result["is_balanced"],
            "message": "Estructura del árbol AVL"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener la estructura del árbol: {str(e)}"
        )

# 4. Endpoint para verificar el balance del árbol
@router.get("/tree/balance")
async def check_balance():
    try:
        result = avl_service.check_balance()
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result["message"]
            )
            
        return {
            "status": "success",
            "is_balanced": result["is_balanced"],
            "message": result["message"]
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al verificar el balance del árbol: {str(e)}"
        )

# 5. Endpoint para limpiar el árbol
@router.delete("/tree", status_code=status.HTTP_200_OK)
async def clear_tree():
    try:
        result = avl_service.clear_tree()
        
        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result["message"]
            )
            
        return {
            "status": "success",
            "message": result["message"]
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al limpiar el árbol: {str(e)}"
        )
        

