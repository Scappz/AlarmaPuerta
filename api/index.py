from flask import Flask
from vercel import KV

app = Flask(__name__)
kv = KV()


@app.get("/estado")
async def estado():
    value = await kv.get("estado")
    return {"estado": value}


@app.get("/toggle")
async def toggle():
    current_value = await kv.get("estado")
    new_value = "false" if str(current_value).lower() == "true" else "true"
    await kv.put("estado", new_value)
    return {"estado": new_value}
