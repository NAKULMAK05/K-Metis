from fastapi import APIRouter

router = APIRouter()


@router.post("/run/{doc_id}")
async def run_extract(doc_id: str):
    # Stub: regex/parsers then LLM JSON schema with ECA consensus
    return {"doc_id": doc_id, "status": "queued"}


