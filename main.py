from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    course: str

students = []

@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": f"Student {student.name} added successfully"}



