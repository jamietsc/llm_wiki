# 🗺️ Project Roadmap: AI Knowledge Hub

This roadmap outlines the iterative, "Local-First" evolution of the AI-native Wiki project — from a simple in-memory script to a fully containerized, cloud-ready enterprise application.

---

## 🟢 Phase 1: Core Retrieval & Vector Search (Completed / In Progress)
*Focus: Understanding math, embeddings, and basic retrieval logic without external overhead.*
- [x] Establish repository documentation and architecture design (`ARCHITECTURE_IDEAS.md`).
- [x] Implement document reading from local storage.
- [x] Implement Document-Structure Chunking (header-based splitting at `#` / `##`).
- [x] Introduce clean object-oriented data structures.
- [x] Integrate local embedding model (`BAAI/bge-m3` via `sentence-transformers`).
- [x] Implement In-Memory Cosine Similarity search and Top-$K$ ranking.
- [x] Enhance terminal output to display source grounding (showing the exact Wikipedia source file and match score).

## 🟡 Phase 2: Modularization, Metadata & Source Grounding
*Focus: Clean software architecture, code organization, and preparing for generation.*
- [ ] Split monolithic script into dedicated Python modules, for e.g.:
  - `ingestion.py` (File loading & chunking)
  - `embedder.py` (Model handling & vectorization)
  - `retriever.py` (Similarity search & ranking)
  - `main.py` (Orchestration)

- [x] **Optional/Teaser:** Connect a local LLM via Ollama (e.g., Qwen or Gemma) to synthesize the retrieved chunks into a final natural-language answer.

## 🟠 Phase 3: Backend API & Database Migration (`pgvector`)
*Focus: Transitioning from local memory to an enterprise-grade database and backend service.*
- [ ] Set up PostgreSQL with the `pgvector` extension (locally or via lightweight setup).
- [ ] Implement data ingestion pipeline to store chunks and vector embeddings directly into PostgreSQL.
- [ ] Build a REST API wrapper around the retrieval logic using **FastAPI** (Python) or **ASP.NET Core** (C#).
- [ ] Test API endpoints via Swagger UI / Postman (e.g., `/search` and `/ask`).

## 🔵 Phase 4: Containerization & Docker Compose
*Focus: Environment isolation, reproducibility, and modern deployment practices.*
- [ ] Write a `Dockerfile` for the backend application.
- [ ] Set up a `docker-compose.yml` orchestrating:
  - The PostgreSQL + `pgvector` database container.
  - The Backend API container.
- [ ] Verify that the entire stack spins up with a single command (`docker compose up`).

## 🟣 Phase 5: Frontend UI & Cloud Infrastructure (Portfolio Veredelung)
*Focus: Usability, full-stack integration, and Infrastructure as Code (IaC).*
- [ ] Build a lightweight Frontend (e.g., Streamlit, Blazor, or a clean web UI) featuring:
  - A Markdown editor for manual article creation.
  - An LLM-assisted generation/expansion mode.
  - Live source citation view.
- [ ] Write Infrastructure as Code (IaC) templates (e.g., Terraform or Bicep) to describe cloud deployment (e.g., Azure Container Apps / App Service).
- [ ] Finalize repository documentation with architecture diagrams and setup instructions for GitHub.
- [ ] Add a configuration page to the frontend, to configure model path, file path and database path