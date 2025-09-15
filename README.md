## K-METIS (KMRL Evidence-Anchored, Trustworthy Intelligence Summaries) — MVP

An end-to-end MVP delivering evidence-anchored document intelligence with OCR, deterministic parsing, consensus-based ECA, a Neo4j knowledge graph, Elasticsearch retrieval, and a modern React UI.

### Tech Stack
- Frontend: React + Vite + TailwindCSS + Shadcn UI (skeleton) + Framer Motion
- Backend: FastAPI (Python)
- OCR: Sarvam.ai (if available), Tesseract, Google Vision, Google Document AI
- Graph DB: Neo4j
- Search: Elasticsearch
- Storage: MinIO (S3-compatible)
- Logs/Events: PostgreSQL
- Messaging: MQTT Sparkplug-B (UNS)
- Deployment: Docker Compose (Kubernetes-ready structure)

### Quickstart
1) Copy environment template and adjust values:
```bash
cp .env.example .env
```
2) Start services:
```bash
docker compose up -d --build
```
3) Open services:
- Backend API: `http://localhost:8000/docs`
- Frontend UI: `http://localhost:5173`
- Neo4j Browser: `http://localhost:7474` (neo4j/neo4j; change password at first login)
- MinIO Console: `http://localhost:9001` (minioadmin/minioadmin)
- Postgres: `localhost:5432` (see `.env`)
- Elasticsearch: `http://localhost:9200`
- MQTT (Mosquitto): `localhost:1883`

### Repository Structure
```
backend/
  app/
    routers/
    services/
    models/
    utils/
    main.py
    config.py
    deps.py
  requirements.txt
  Dockerfile
frontend/
  src/
  index.html
  package.json
  vite.config.ts
  tailwind.config.ts
  postcss.config.js
  Dockerfile
docker-compose.yml
.env.example
.gitignore
```

### MVP Scope Coverage
- Ingestion: Upload API + raw storage in MinIO; doc nodes in Neo4j
- OCR: Pipeline with Sarvam/Tesseract/Vision/DocAI stubs & fallback
- Parsing/Extraction: Deterministic regex/parsers first, LLM JSON schema fallback
- ECA: Redundant extractors, consensus, verifier micro-agents (stubs), quarantine/commit
- Graph: Neo4j schema and linker service
- Retrieval: Elasticsearch indexing + Neo4j Cypher querying
- Summarizer: Evidence Cards with anchors to source locations
- Routing & UNS: MQTT Sparkplug-B publisher (skeleton)
- Provenance: C2PA/VC stubs, provenance badges wiring endpoints
- UI: Upload, PDF viewer, Evidence Cards, Audit log, role tabs (skeleton)

### Development
- Backend dev: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Frontend dev: `cd frontend && npm i && npm run dev`

### Security & Compliance (MVP)
- MinIO bucket is created on boot; set immutable bucket policies in production.
- C2PA signing and VC issuance are stubbed; integrate real keys, HSM/CloudKMS.
- Store ECA verification logs and provenance in Postgres.

### Kubernetes
This repo is compose-first with clear boundaries; porting to Kubernetes is straightforward by mapping each service to a Deployment/StatefulSet and wiring Secrets/ConfigMaps.

### Sprint Plan (6 weeks)
- Sprint 0: Dataset and labeling
- Sprint 1: Ingest + storage + Neo4j docs
- Sprint 2: OCR + parsers
- Sprint 3: Extractor + ECA + Linker
- Sprint 4: Summarizer + Retriever + QA
- Sprint 5: UI integration
- Sprint 6: UNS publishing + pilot


