"""
Which Method Is Best?
Here are a few recommendations:
• When passing arguments in the URL, following RESTful guidelines is standard
practice.
• Query strings are usually used to provide optional arguments, like pagination.
• The body is usually used for larger inputs, like whole or partial models.
In each case, if you provide type hints in your data definitions, your arguments will
be automatically type-checked by Pydantic. This ensures that they’re both present and
correct.
"""
import requests
from fastapi import  FastAPI,Request, Response, Header, Query, Body, HTTPException
import uvicorn

app = FastAPI()


# @app.get("/hi")
# def greet():
#     return "Hello World"
#
# @app.get("/hi/{who}")
# def greet(who: str):
#     return f"Hello {who}!"

# =========== second part =====

# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello? {who}?"


# if __name__ == "__main__":
#     uvicorn.run("hello:app",
#               host="0.0.0.0",
#               port=8000,
#               reload=True,)


# ========= third part =======

# @app.get("/hi")
# def greet():
#     return "Hello World"
#
# @app.get("/hi/{who}")
# def greet_with_name(who: str):
#     return f"Hello {who}!"
@app.get("/hi")
def greet(who: str = Query(None, description="Who to greet")):
    print(f"{who=}")
    if who:
        return {"who": f"Hello? {who}?"}
    else:
        return {"who": "Hello World"}

# @app.post("/agent")
# def get_agent(user_agent: str = Header(None, convert_underscores=False)):
#     return user_agent

@app.get("/agent")  # http://0.0.0.0:8000/agent?user_agent=Hallo%20World
def get_agent(user_agent: str = Query(None, description="User-Agent")):
    return user_agent

@app.get("/happy")
def happy():
    return Response(content=";)", status_code=250)

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response, request: Request):
    response.headers[name] = value
    print(f"{value=} {name=} {request.scope=} {response.headers=}", end='\n\p')
    return "normal body"

if __name__ == "__main__":
    uvicorn.run("hello:app",
              host="0.0.0.0",
              port=8000,
              reload=True,)
