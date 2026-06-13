"""idp-svc-demo-5245 — a FastAPI service scaffolded by the IDP."""
from fastapi import FastAPI

app = FastAPI(title="idp-svc-demo-5245")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok", "service": "idp-svc-demo-5245"}


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "idp-svc-demo-5245"}
