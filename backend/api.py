import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-all-teams")
async def get_all_teams():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="ipl_cricket"
)
    cursor = connection.cursor()

    # Example: Execute a query
    cursor.execute("SELECT * FROM teams")

    # Fetch the results
    results = cursor.fetchall()
    return results
