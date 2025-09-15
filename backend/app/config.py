from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    app_secret: str = "dev-secret"

    neo4j_uri: str = "bolt://neo4j:7687"
    neo4j_username: str = "neo4j"
    neo4j_password: str = "neo4j"

    database_url: str = "postgresql+psycopg://kmrl:kmrl_password@postgres:5432/kmrl_kmetis"

    minio_endpoint: str = "minio:9000"
    minio_root_user: str = "minioadmin"
    minio_root_password: str = "minioadmin"
    minio_bucket: str = "kmrl-raw"

    elastic_host: str = "http://elasticsearch:9200"

    mqtt_broker_host: str = "mosquitto"
    mqtt_broker_port: int = 1883

    class Config:
        env_file = ".env"


settings = Settings()


