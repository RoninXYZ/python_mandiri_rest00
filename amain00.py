
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DB = Path("database")
DB.mkdir(exist_ok=True)

FILE = DB / "gps.json"


class GPS(BaseModel):
    device_id: str
    latitude: float
    longitude: float


@app.post("/gps")
def receive_gps(gps: GPS):

    # Simpan data
    with FILE.open("a", encoding="utf-8") as f:
        f.write(
            json.dumps(gps.model_dump()) + "\n"
        )

    return {
        "status": "success",
        "message": "GPS berhasil diterima"
    }
