from fastapi import FastAPI
from app.api.v1.endpoints import items, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include Routers
app.include_router(items.router, prefix="/api/v1/items", tags=["Items"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Project!"}
