from fastapi import FastAPI
from app.api.agents import router as agents_router
from app.api.users import router as users_router

app = FastAPI(
    title="AI Agent Platform",
    version="1.0.0",
)


app.include_router(
    agents_router,
    prefix="/agents",
    tags=["Agents"],
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)
