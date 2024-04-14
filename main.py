from fastapi import FastAPI
from repository.database import initialize_database
from routes import router as api_router

app = FastAPI()
# Inicializa o banco de dados
initialize_database()
# Inclua as rotas definidas no arquivo routes.py
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
