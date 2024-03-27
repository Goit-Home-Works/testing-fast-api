from fastapi import  FastAPI
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

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"


if __name__ == "__main__":
    uvicorn.run("hello:app",
              host="0.0.0.0",
              port=8000,
              reload=True,)
