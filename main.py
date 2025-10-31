from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db, engine
from src.models import Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    return { "message": "Postgres Connection OK!" }
