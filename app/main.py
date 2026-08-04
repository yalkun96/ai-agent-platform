from fastapi import FastAPI
from app.api.agents import router as agents_router

app = FastAPI(
    title="AI Agent Platform",
    version="1.0.0",
)


app.include_router(
    agents_router,
    prefix="/agents",
    tags=["Agents"],
)
