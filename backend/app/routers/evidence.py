from fastapi import APIRouter

router = APIRouter()


@router.get("/card/{doc_id}")
async def get_evidence_card(doc_id: str):
    # Stub: return a minimal evidence card structure
    return {
        "doc_id": doc_id,
        "summary": "MVP evidence card",
        "obligations": [],
        "risks": [],
        "deadlines": [],
        "anchors": [],
        "provenance": {"c2pa": None, "vc": None},
    }


