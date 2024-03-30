import uvicorn
from fastapi import FastAPI, Depends, Query, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

# the dependency function:
def user_dep(name: str = Query(default=None), password: str = Query(default=None)):
    return {"name": name, "valid": True}

# the dependency function for checking input
def check_dep(name: str = Query(default=None), password: str = Query(default=None)):
    if not name:
        raise ValueError("Name is required")

# the path function / web endpoint:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# the path function / web endpoint:
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True

# Exception handler for handling ValueError
@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"message": str(exc)})

if __name__ == "__main__":
    uvicorn.run("dependency:app",
                host="0.0.0.0",
                port=8000,
                reload=True)
