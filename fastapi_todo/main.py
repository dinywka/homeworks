from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from datetime import datetime
import sqlite3
from starlette.responses import HTMLResponse, RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DB_FILE = "mydatabase.db"

def create_table():
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                datetime DATE
            )
        """)
        print("Table 'posts' created or already exists.")
    except sqlite3.Error as e:
        print("Error while creating or connecting to the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")


@app.on_event("startup")
async def startup():
    create_table()


@app.get("/")
async def home(request: Request):
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, description, datetime FROM posts")
        rows = [{"id": row[0], "description": row[1], "datetime": row[2]} for row in cursor.fetchall()]
        return templates.TemplateResponse("list.html", {"request": request, "list": rows})
    except sqlite3.Error as e:
        print("Error while fetching posts from the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")


# @app.get("/list")
# async def list_posts(request: Request):
#     connection = sqlite3.connect(DB_FILE)
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id, description, datetime FROM posts")
#         rows = [{"id": row[0], "title": row[1], "description": row[2], "datetime": row[3]} for row in cursor.fetchall()]
#         return templates.TemplateResponse('list.html', {"request": request, "list": rows})
#     except sqlite3.Error as e:
#         print("Error while fetching posts from the 'posts' table:", e)
#     finally:
#         cursor.close()
#         connection.close()
#         print("SQLite connection is closed")


@app.get("/create", response_class=RedirectResponse)
async def view_create(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/create")
async def create_post(request: Request, description: str = Form(...)):
    date = datetime.now().strftime("%Y-%m-%d")
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO posts (description, datetime) VALUES (?, ?)"
        values = (description, date)
        cursor.execute(query, values)
        connection.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error while inserting data into the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")
    return RedirectResponse(url=app.url_path_for("home"), status_code=303)


@app.get("/change", response_class=HTMLResponse)
async def view_change(request: Request):
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        pk = int(request.query_params.get("pk"))
        query = "SELECT id, description, datetime FROM posts WHERE id = ?"
        values = (pk,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        if row:
            post = {"id": row[0], "description": row[1], "datetime": row[2]}
            return templates.TemplateResponse("change.html", {"request": request, "post": post})
        else:
            return RedirectResponse(url="/")
    except sqlite3.Error as e:
        print("Error while fetching post from the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")


@app.post("/change", response_class=RedirectResponse)
async def change_post(request: Request):
    date = datetime.now().strftime("%Y-%m-%d")
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        form = await request.form()
        pk = form.get('pk')
        description = form.get('description')
        query = "UPDATE posts SET description = ?, datetime = ? WHERE id = ?"
        values = (description, date, pk)
        cursor.execute(query, values)
        connection.commit()
        print("Data updated successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error while updating data in the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")
    return RedirectResponse(url=app.url_path_for("home"), status_code=303)


@app.get("/delete", response_class=RedirectResponse)
async def view_delete(request: Request):
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        query = "DELETE FROM posts WHERE id = ?"
        pk = int(request.query_params.get("pk"))
        values = (pk,)
        cursor.execute(query, values)
        connection.commit()
        print("Data deleted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error while deleting data from the 'posts' table:", e)
    finally:
        cursor.close()
        connection.close()
        print("SQLite connection is closed")
    return RedirectResponse(url="/")





if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
