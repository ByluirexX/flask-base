from sqlalchemy.orm import Session
from myapp.task import models
from myapp import db
def getById(id: int):
    #task = db.session.query(models.Task).filter(models.Task.id == id).first()
    task = db.session.query(models.Task).get(id)
    #task = models.Task.query.get_or_404(id) 
    return task
    
def getAll():
    tasks = db.session.query(models.Task).all()
    return tasks
def create(name: str):
    taskdb = models.Task(name=name)
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb
def update(id:int, name: str):
    taskdb = getById(id=id)
    
    taskdb.name = name
    
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb
    
    
def delete(id:int):
    taskdb = getById(id=id)
    db.session.delete(taskdb)
    db.session.commit()
    
def pagination(page:int=1, size:int=10):
    taskdb = models.Task.query.paginate(page=page, per_page=size)
    return taskdb