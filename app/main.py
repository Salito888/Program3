
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.AVL_controller import router as avl_router

app = FastAPI(
    title="API Árbol AVL",
    description="API para gestión de niños usando una estructura de árbol AVL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplaza con los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # O especifica los métodos permitidos: ["GET", "POST", "DELETE"]
    allow_headers=["*"],
)


app.include_router(avl_router, prefix="/api/v1")

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "¡Bienvenido a la API del Árbol AVL!",
        "documentation": "/docs",
        "endpoints": {
            "add_child": "POST /api/v1/child",
            "get_child": "GET /api/v1/child",
            "get_child": "GET /api/v1/child/{id}",
            "get_tree": "GET /api/v1/tree",
            "clear_tree": "DELETE /api/v1/tree"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",  
        port=8000,
        reload=True
    )
