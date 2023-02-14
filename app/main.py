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
    data = db_cursor.get_posts(table="posts")
    return {"posts": data}


@app.get("/posts/{post_id}")
def get_all_posts(post_id: int):
    data = db_cursor.get_posts(table="posts", post_id=str(post_id))
    return {"posts": data}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def insert_post(post: Post):
    return db_cursor.insert_post(post)

