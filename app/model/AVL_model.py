
from typing import Optional, Dict, Any
from pydantic import BaseModel

class Child(BaseModel):
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

class AVLNode:
    def __init__(self, child: Child):
        self.child = child
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height = 1
        self.balance = 0
    
    def update_height_and_balance(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)
        self.balance = left_height - right_height
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "child": self.child.to_dict() if self.child else None,
            "height": self.height,
            "balance": self.balance,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def insert(self, child: Child) -> None:
        self.root = self._insert_recursive(self.root, child)
    
    def _insert_recursive(self, node: Optional[AVLNode], child: Child) -> AVLNode:
        if not node:
            return AVLNode(child)
        
        if child.id < node.child.id:
            node.left = self._insert_recursive(node.left, child)
        elif child.id > node.child.id:
            node.right = self._insert_recursive(node.right, child)
        else:
            return node
        
        node.update_height_and_balance()
        return self._balance(node)
    
    def _balance(self, node: AVLNode) -> AVLNode:
        if node.balance > 1 and node.left and node.left.balance >= 0:
            return self._rotate_right(node)
        
        if node.balance < -1 and node.right and node.right.balance <= 0:
            return self._rotate_left(node)
        
        if node.balance > 1 and node.left and node.left.balance < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        if node.balance < -1 and node.right and node.right.balance > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right if x else None
        
        if x:
            x.right = y
        y.left = T2
        
        y.update_height_and_balance()
        if x:
            x.update_height_and_balance()
        
        return x if x else y
    
    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left if y else None
        
        if y:
            y.left = x
        x.right = T2
        
        x.update_height_and_balance()
        if y:
            y.update_height_and_balance()
        
        return y if y else x
    
    def find_by_id(self, id: int) -> Optional[Child]:
        return self._find_recursive(self.root, id)
    
    def _find_recursive(self, node: Optional[AVLNode], id: int) -> Optional[Child]:
        if not node:
            return None
        
        if id < node.child.id:
            return self._find_recursive(node.left, id)
        elif id > node.child.id:
            return self._find_recursive(node.right, id)
        else:
            return node.child
    
    def to_dict(self) -> Dict[str, Any]:
        return self.root.to_dict() if self.root else {}
    
    def is_balanced(self) -> bool:
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node: Optional[AVLNode]) -> bool:
        if not node:
            return True
        
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        
        return (abs(left_height - right_height) <= 1 and 
                self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))
    
    def clear(self) -> None:
        self.root = None
        
