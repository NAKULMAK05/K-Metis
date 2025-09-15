from fastapi import APIRouter

router = APIRouter()


@router.post("/run/{doc_id}")
async def run_ocr(doc_id: str):
    # Stub: enqueue OCR pipeline (Sarvam -> Tesseract -> Vision -> DocAI fallback)
    return {"doc_id": doc_id, "status": "queued"}


