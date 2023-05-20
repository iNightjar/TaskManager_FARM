from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # cross origin resoure sharing.

from fastapi import HTTPException
from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo
)

# import the Todo Model
from model import Todo

# app object

app = FastAPI()


<<<<<<< Updated upstream
origings = ['http://localhost:3000'] # allowd hosts to see our endpoints
=======
origings = ['http://localhost:3000']
>>>>>>> Stashed changes

app.add_middleware(
    CORSMiddleware,
    allow_origins= origings,
    allow_methods=['*'],
    allow_headers = ['*'],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}

# Perform CRUD Operations as much as we want,,

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response: # response is True
        return response
    raise HTTPException(404, f" *** // THERE IS NO TODO ITEM WITH THIS TITLE => {title}, PLEASE CHECK ASAP // *** ") # request status = not found

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    # convert JSON object to DICT
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, f" *** // SOMETHING WENT WRONG // *** ") # request status = bad request



@app.put("/api/todo{title}/", response_model=Todo)
async def put_todo(title: str, desc:str):
    response = await update_todo(title, desc)
    if response: # Response returned succesfully
        return response
    raise HTTPException(404, f" *** // THERE IS NO TODO ITEM WITH THIS TITLE => {title}, PLEASE CHECK ASAP // *** ") # this todo is not in our db




@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return " *** // SUCCESFULLY DELETED THIS ITEM // *** "
    raise HTTPException(404, f" *** // THERE IS NO TODO ITEM WITH THIS TITLE => {title}, PLEASE CHECK ASAP // *** ") # this todo is not in our db
