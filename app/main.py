from fastapi import FastAPI, status, HTTPException
from utils.postgres.query_postgres import QueryPG
from schema.schema import Post


app = FastAPI()
db_cursor = QueryPG()


@app.get('/')
def home():
    return "API is up and running"


@app.get("/posts")
def get_all_posts():
    data = db_cursor.execute_query("SELECT * FROM posts")
    return {"posts": data}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def insert_post(post: Post):
    return db_cursor.insert_post(post)

