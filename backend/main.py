from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import YellEntry
from database import get_connection, create_table
from datetime import datetime

app = FastAPI()
create_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add-yell")
def add_yell(entry: YellEntry):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute("""
                   INSERT INTO yells(who_yelled, reason, count, timestamp) VALUES (?,?,?,?)""",(entry.who_yelled, entry.reason,entry.count,timestamp))
    conn.commit()
    conn.close()
    return {"message":"Your anger has been registered"}
    
@app.post("/get-yells")
def get_yells():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM yells order by timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

