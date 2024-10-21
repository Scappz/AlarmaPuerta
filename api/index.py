from flask import Flask
from vercel_kv_sdk import KV

app = Flask(__name__)
kv = KV()


def parse_bool(strval):
    return str(strval).lower() == "true"


@app.get("/estado")
def estado():
    value = parse_bool(kv.get("estado"))
    return {"estado": value}


@app.get("/toggle")
def toggle():
    value = parse_bool(kv.get("estado"))
    kv.set("estado", not value)
    return {"estado": not value}
