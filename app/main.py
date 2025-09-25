from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time

app = FastAPI()
REQS = Counter("demo_requests_total", "Total requests", ["path"])

@app.get("/healthz")
def health():
    REQS.labels("/healthz").inc()
    return {"ok": True}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/cpu")
def cpu_burn(seconds: int = 2):
    """
    Burns CPU for `seconds` to simulate load.
    """
    REQS.labels("/cpu").inc()
    start = time.time()
    while time.time() - start < seconds:
        # Tight loop does pointless math to consume CPU
        _ = [x**2 for x in range(1000)]
    return {"message": f"Burned CPU for {seconds} seconds"}
