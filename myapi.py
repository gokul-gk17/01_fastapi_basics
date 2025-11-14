from fastapi import FastAPI,Path
from typing import Optional 
from pydantic import BaseModel
app=FastAPI()

students = {
    1: {
        "name" : "Gokul",
        "age" : 20,
        "Section" : "CG"
    },
        2: {
        "name": "Meera",
        "age": 19,
        "Section": "CF"
    },
    3: {
        "name": "Arjun",
        "age": 21,
        "Section": "CY"
    },
    4: {
        "name": "Sanjay",
        "age": 22,
        "Section": "CG"
    },
    5: {
        "name": "Lakshmi",
        "age": 20,
        "Section": "CF"
    },
    6: {
        "name": "Hari",
        "age": 18,
        "Section": "CZ"
    }
}

class Student(BaseModel):
    name:str
    age:int
    section:str

class UpdatedStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    section:Optional[str]=None


@app.get('/')
def index():
    return {"Welcome to First FastAPI Output"}


@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path(...,description="The ID of the student you want to view",gt=0)):
    return students[student_id]


@app.get('/get-student-name/{student_id}')
def get_student_name(*,student_id :int= Path(...,description="The ID of the student you want to view",gt=0),name:Optional[str] = None,age:int):
    for student_id in students:
        if students[student_id]['name']== name:
            return students[student_id]
    return {"Data not found"}


@app.post('/create-student/{student_id}')
def create_student(student_id:int,student : Student):
    if( student_id in students):
        return {"Error":"Student ID already exists"}
    students[student_id]=student
    return students[student_id]

@app.put('/Update-student/{student_id}')
def update_student(student_id:int,student:UpdatedStudent):
    if student_id not in students:
        return {'Error : Student ID not found'}
    
    if student.name != None:
        students[student_id]["name"]=student.name
    if student.age != None:
        students[student_id]["age"]=student.age
    if student.section != None:
        students[student_id]["section"]=student.section

    return students[student_id]





