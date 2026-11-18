from fastapi import FastAPI
from course_service import courses

app = FastAPI()

@app.get("/welcome")
def wecome_msg():
    return {
        "message" : "Welcome Latika"
    }

@app.get("/greet")
def greet_msg():
    return {
        "message" : "Welcome to FastApI"
    }  

@app.get("/courses")
def get_courses():
    return courses

@app.get("/courses/{course_id}")
def course_by_id(course_id:int):
    course = courses.get(course_id)    

    if course is None:
        raise HHTPException(
            status_code = 400,
            detail = "Course is not Found"
        )
    return courses   

@app.get("/course")
def course_by_id(course_id:int):
    course = courses.get(course_id)    

    if course is None:
        raise HHTPException(
            status_code = 400,
            detail = "Course is not Found"
        )
    return courses 