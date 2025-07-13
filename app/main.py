from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/db")
def check_db():
    try:
        conn = psycopg2.connect(
            host="postgres",
            user="admin",
            password="admin123",
            dbname="meubanco"
        )
        conn.close()
        return {"status": "connected to PostgreSQL"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
