from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import ingest, ocr, extract, evidence, retrieve


def create_app() -> FastAPI:
    app = FastAPI(title="K-METIS API", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
    app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])
    app.include_router(extract.router, prefix="/extract", tags=["extract"])
    app.include_router(evidence.router, prefix="/evidence", tags=["evidence"])
    app.include_router(retrieve.router, prefix="/retrieve", tags=["retrieve"])

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()


