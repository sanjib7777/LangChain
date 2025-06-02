from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name: str = Field(..., description="The name of the student")
    email: EmailStr = Field(..., description="The email address of the student")

new_student = Student(name="Sanjib Shah", email="sanjib.shah@example.com")
student = Student(**new_student.dict())  # This will raise an error since 'age' is not defined in the Student model
print(student)