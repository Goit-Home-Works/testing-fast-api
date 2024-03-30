from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def greeting(request):
    return JSONResponse('Hello? World?')

app = Starlette(debug=True, routes=[
    Route('/hi', greeting),
])

# type hints: float, str, tuple, .....

physics_magic_number: float = 1.0/137.03599913
hp_lovecraft_noun: str = "ichor"
exploding_sheep: tuple = "sis", "boom", "bah!"
responses: dict = {"Marco": "Polo", "answer": 42}

print(f"{exploding_sheep =}")  # exploding_sheep =('sis', 'boom', 'bah!')


# uvicorn starlette_hello:app

# http://localhost:8000/hi

#  git:(main) ✗ uvicorn starlette_hello:app
# exploding_sheep =('sis', 'boom', 'bah!')
# INFO:     Started server process [1053699]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     127.0.0.1:37120 - "GET /docs HTTP/1.1" 404 Not Found
# INFO:     127.0.0.1:37136 - "GET /hi HTTP/1.1" 200 OK

