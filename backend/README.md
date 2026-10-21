# LLM Wiki

An AI-native knowledge base & wiki system built with Python, Qdrant and RAG architecture.
Allows users to co-create documentation with LLM assistance or generate context-aware articles automatically.

---

## Key Features
* **Hybrid Editing:** Write manually or prompt the LLM to draf/expand sections.
* **Context-Aware RAG:** Answers questions and generates text based on indexed wiki documents.
* **Source Grounding:** Generates citations and links back to irginal articless.
* **Local-First & Privacy-Focused:** Run completely offline using local LLMs

## 🛠 Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastAPI
* **Vector Database:** Qdrant
* **Embeddings & LLM:** Hugging Face / Ollama / Local Qwen
* **Containerization:** Docker & Docker Compose (Planned for Phase 3)

---

## 🚀 Roadmap
- [x] Initial Repository & Architecture Planning
- [ ] **Phase 1:** Core RAG & Vector Search Proof of Concept (In-Memory)
- [ ] **Phase 2:** Modular Backend API (FastAPI)
- [ ] **Phase 3:** Dockerization & Multi-Container Setup
- [ ] **Phase 4:** UI Integration & Cloud IaC (Terraform)