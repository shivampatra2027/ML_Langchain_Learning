from typing import Optional

from pydantic import BaseModel, EmailStr, Field
class Student(BaseModel):
        name:str='sp'
        age:Optional[int]=None
        email:EmailStr
        cgpa:float=Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student')

new_student={'name':'sp',
    'age':21,
    'email':'abc@gmail.com'
}

student=Student(**new_student)
print(student.cgpa)

student_json = student.model_dump_json()
