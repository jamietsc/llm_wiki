# Architecture Ideas & Design Decisions

## 1. Feature Ideas
* **Automated Article Summarization:** When an article becomes to long click a button to generate an executive summary.
* **Clonflict Detection:** Warn the user if a new wiki entry contradicts an existing entry in the vector store.
* **Markdown Formatting Rules:** Force the LLM to strictly return valid Markdown.

## 2. Optional Technical Questions
* **Chunking Strategy:** Fixed-size chunking (e.g., 500 tokens) vs. Markdown-heading-aware chunking?

## 3. Tech-Stack
### Vector Database:
For this project I will use **pgvector** which is an extension for PostgreSQL. It adds the data type ```vector``` to the database, which allows embeddings, numerical representation of text, images or other content. 
<br>
The reason why I am using this is because it is a free and open-source database which is often used for machine learning models.
<br>
*Note for Phase 1:* A lightweight In-Memory vector store will be used for rapid prototyping. 

### Chunking Model:
For this project I will use **Document-Structure Chunking**. The wiki page will be splitted at each header, so that every section becomes it own chunk.
<br>
The reason why I am using this strategy is because the wiki is already organized. There is no reasing to cut a sentence in the middle, when the wiki is already structured.

### Embedding model:
For this project I will use the **bge-m3** embedding model. 
<br>
The reason why I am using this model, is becuase of the scaling and the hybrid search. The model supports dense and thin vectors. It is perfect for wikis, because it finds keywoards and the meaning.   

### Similarity metrics:
For this project I will use the **Cosine Similarity**.
<br>
The reason for this is, it compares the angles between two vectors, which is the standard for text-embedding und a perfect match for ```bge-m3```


## 4. Decision Log (ADR)
* **2026-10-08:** Decided to build a "Local-First" prototype to unterstand RAG mechanisms before touching the technology with deeper meaning.