from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
from minio import Minio
from minio.error import S3Error
from ..config import settings
from ..deps import get_neo4j_session


router = APIRouter()


def get_minio_client() -> Minio:
    endpoint = settings.minio_endpoint
    host, port = endpoint.split(":")
    return Minio(
        f"{host}:{port}",
        access_key=settings.minio_root_user,
        secret_key=settings.minio_root_password,
        secure=False,
    )


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    client = get_minio_client()
    bucket = settings.minio_bucket
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)

    doc_id = str(uuid4())
    object_name = f"raw/{doc_id}/{file.filename}"
    try:
        client.put_object(bucket, object_name, file.file, length=-1, part_size=10 * 1024 * 1024)
    except S3Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Create Neo4j node for document
    for session in get_neo4j_session():
        session.run(
            "MERGE (d:Document {id: $id}) SET d.filename=$filename, d.object=$object, d.status=$status",
            id=doc_id,
            filename=file.filename,
            object=object_name,
            status="uploaded",
        )

    return {"id": doc_id, "object": object_name}


