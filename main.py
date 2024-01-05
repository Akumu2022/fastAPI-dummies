from fastapi import FastAPI, Path

app = FastAPI() #initialize

employees = {
    1: {
        "name":"Akumu Wycliff",
        "role":"Software Engineer",
        "salary":2000000
    },
    2: {
        "name":"Juulian Wepukhulu",
        "role":"Software Engineer",
        "salary":2000000
    },
     3: {
        "name":"Karanja Wanjala",
        "role":"Backend Engineer",
        "salary":500000
    },
      3: {
        "name":"Karanja Wanjala",
        "role":"Backend Engineer",
        "salary":500000
    },
    
}

@app.get("/")
def index():
    return{"name":"Akumu Wycliff"}

@app.get("/get_employee/{employee_id}") #here we basically define the function behavior or work
def get_employee(employee_id: int):
    return employees[employee_id] # concept path parameter


@app.get("/get_by_name")
def get_employee(name : str):
    for employee_id in employees:
        if employees[employee_id][name] == name:
            return employees[employee_id]
    return{"Data":"Not found"}    
