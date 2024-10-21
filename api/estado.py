from fastapi import FastAPI
from vercel import KV
from contextlib import asynccontextmanager

app = FastAPI()
kv = KV()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kv.put("estado", "true")
    yield


@app.get("/get_estado")
async def get_estado():
    value = await kv.get("estado")
    return {"estado": value}


@app.put("/toggle_estado")
async def toggle_estado():
    current_value = await kv.get("estado")
    new_value = "false" if str(current_value).lower() == "true" else "true"
    await kv.put("estado", new_value)
    return {"estado": new_value}
