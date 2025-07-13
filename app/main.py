from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.60:8282/db"],  # ou ["http://192.168.1.60:8282"] se quiser mais seguro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pega a variável do deployment
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria engine de conexão com o banco
engine = create_engine(DATABASE_URL, echo=True)

@app.get("/")
def read_root():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 'Conexão com o banco de dados funcionando!'"))
            message = result.scalar()
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8181)
