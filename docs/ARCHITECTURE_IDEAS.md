# Architecture Ideas & Design Decisions

## 1. Feature Ideas
* **Automated Article Summarization:** When an article becomes to long click a button to generate an executive summary.
* **Clonflict Detection:** Warn the user if a new wiki entry contradicts an existing entry in the vector store.
* **Markdown Formatting Rules:** Force the LLM to strictly return valid Markdown.

## 2. Optional Technical Questions
* **Chunking Strategy:** Fixed-size chunking (e.g., 500 tokens) vs. Markdown-heading-aware chunking?

## 3. Decision Log (ADR)
* **2026-10-08:** Decided to build a "Local-First" prototype to unterstand RAG mechanisms before touching the technology with deeper meaning.