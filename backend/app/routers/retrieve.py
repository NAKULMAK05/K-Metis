from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/search")
async def search(q: str = Query(..., min_length=1)):
    # Stub: Elasticsearch keyword recall + Neo4j deterministic answers
    return {"query": q, "results": []}


