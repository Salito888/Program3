
from typing import Dict, Any
import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from model.AVL_model import AVLTree, Child


class AVLService:
    def __init__(self):
        self.tree = AVLTree()
    
    def insert_child(self, id: int, name: str, age: int) -> Dict[str, Any]:
        try:
            if self.tree.find_by_id(id) is not None:
                return {
                    "success": False,
                    "message": f"Ya existe un niño con la identificación {id}"
                }
            
            new_child = Child(id, name, age)
            self.tree.insert(new_child)
            
            return {
                "success": True,
                "message": "Niño agregado correctamente",
                "child": new_child.to_dict(),
                "is_balanced": self.tree.is_balanced()
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al insertar el niño: {str(e)}"
            }
    
    def find_child(self, id: int) -> Dict[str, Any]:
        try:
            child = self.tree.find_by_id(id)
            
            if child is None:
                return {
                    "success": False,
                    "message": f"No se encontró ningún niño con la identificación {id}"
                }
                
            return {
                "success": True,
                "child": child.to_dict()
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al buscar el niño: {str(e)}"
            }
    
    def get_tree(self) -> Dict[str, Any]:
        try:
            tree_data = self.tree.to_dict() if hasattr(self.tree, 'to_dict') else {}
            return {
                "success": True,
                "tree": tree_data,
                "is_balanced": self.tree.is_balanced() if hasattr(self.tree, 'is_balanced') else False
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al obtener el árbol: {str(e)}"
            }
    
    def check_balance(self) -> Dict[str, Any]:
        try:
            is_balanced = self.tree.is_balanced() if hasattr(self.tree, 'is_balanced') else False
            return {
                "success": True,
                "is_balanced": is_balanced,
                "message": "El árbol está balanceado" if is_balanced else "El árbol NO está balanceado"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al verificar el balance: {str(e)}"
            }
    
    def clear_tree(self) -> Dict[str, Any]:
        try:
            self.tree.clear()
            return {
                "success": True,
                "message": "Árbol limpiado correctamente"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al limpiar el árbol: {str(e)}"
            }
