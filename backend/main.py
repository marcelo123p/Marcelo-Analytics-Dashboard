from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect():
    return psycopg2.connect(
        host="localhost",
        database="analytics",
        user="postgres",
        password="Lumar0307"
    )

@app.get("/api/top-products")
def top_products():
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT p.name, SUM(s.quantity) AS total
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        ORDER BY total DESC
        LIMIT 5;
    """)
    data = cur.fetchall()
    conn.close()
    return data

@app.get("/api/revenue")
def revenue():
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT SUM(total_amount) AS total FROM sales;")
    data = cur.fetchone()
    conn.close()
    return data

@app.get("/api/hourly")
def hourly():
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT EXTRACT(HOUR FROM sale_date) AS hour, COUNT(*) AS sales
        FROM sales
        GROUP BY hour
        ORDER BY hour;
    """)
    data = cur.fetchall()
    conn.close()
    return data
