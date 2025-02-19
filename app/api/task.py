from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.requests import Request
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from app.db import Task
from app.db.base import async_get_db

router = APIRouter()
template = Jinja2Templates(directory='app/templates')


class TaskRef(BaseModel):
    name: str
    description: str


class TaskResponse(TaskRef):
    id: int

@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@router.get("/task/edit/{task_id}", response_class=HTMLResponse)
async def edit_task_page(request: Request, task_id: int):
    return template.TemplateResponse("edit_task.html", {"request": request, "task_id": task_id})

@router.get("/task/{task_id}", response_class=HTMLResponse)
async def task_detail_page(request: Request, task_id: int):
    return template.TemplateResponse("task_detail.html", {"request": request, "task_id": task_id})


@router.get("/api/tasks", response_class=JSONResponse)
async def get_all(db: AsyncSession = Depends(async_get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


@router.get("/api/tasks", response_class=JSONResponse)
async def get_all_tasks(db: AsyncSession = Depends(async_get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


@router.get("/api/task/{task_id}", response_model=TaskResponse)
async def get_one_task(task_id: int, db: AsyncSession = Depends(async_get_db)):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found!")
    return task


@router.post("/api/tasks", response_model=TaskResponse)
async def create_task(task: TaskRef, db: AsyncSession = Depends(async_get_db)):
    new_task = Task(name=task.name, description=task.description)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


@router.put("/api/task/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_data: TaskRef, db: AsyncSession = Depends(async_get_db)):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.name = task_data.name
    task.description = task_data.description
    await db.commit()
    await db.refresh(task)
    return task


@router.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(async_get_db)):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(task)
    await db.commit()
    return JSONResponse(content={"message": "Task deleted"})