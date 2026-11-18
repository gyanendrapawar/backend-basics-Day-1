from fastapi import FastAPI, Request

app = FastAPI()


# Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming Request: {request.method} {request.url.path}")

    response = await call_next(request)

    print(f"Outgoing Response: {response.status_code}")

    return response


# GET API
@app.get("/users")
async def get_users():
    return {
        "users": ["Alice", "Bob", "Charlie"]
    }


# POST API
@app.post("/users")
async def create_user(user: dict):
    return {
        "message": "User created",
        "user": user
    }
