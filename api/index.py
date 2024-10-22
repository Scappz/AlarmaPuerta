from flask import Flask, jsonify, request
from vercel_kv_sdk import KV
import os

app = Flask(__name__)
kv = KV()
TOGGLE_SECRET = os.getenv("TOGGLE_SECRET")


def parse_bool(strval):
    return str(strval).lower() == "true"


@app.get("/estado")
def estado():
    value = parse_bool(kv.get("estado"))
    return {"estado": value}


@app.get("/toggle")
def toggle():
    token = request.headers.get("Secret")
    if token != TOGGLE_SECRET:
        return jsonify({"error": "Unauthorized"}), 403

    value = parse_bool(kv.get("estado"))
    kv.set("estado", not value)
    return {"estado": not value}
