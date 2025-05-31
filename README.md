# RAG_AI_Assignment

## 📄 Selected Document
I used the Wikipedia article on Artificial Intelligence:  
https://en.wikipedia.org/wiki/Artificial_intelligence

I extracted the article using a Python script with BeautifulSoup, cleaned the text, and saved it in `Selected_Document.txt`.

---

## 🔍 Five Deep-Dive Questions + Answers

**1. What is embedding dimensionality in this project?**  
We use `paraphrase-MiniLM-L6-v2` which returns 384-dimensional vectors. This affects FAISS indexing performance and retrieval precision.

**2. How does FAISS search for relevant chunks?**  
FAISS uses L2 (Euclidean) distance between the question vector and document chunk vectors to find the closest matches.

**3. Why do chunk_size and chunk_overlap matter?**  
Smaller chunks = more relevant, but less context. Larger chunks = more context, but less focused. Overlap ensures smoother context flow between splits.

**4. How does prompt design impact response quality?**  
The clarity of the context + question combined directly affects how well the language model generates a correct, useful response.

**5. Why use sentence-transformers instead of OpenAI embeddings?**  
Sentence-transformers are free, local, and easy to run. They provide solid performance without relying on paid APIs.

---

## 🧪 Chunk Size & Overlap Findings

- I tried chunk_size values of 300, 500, 800.
- Best results came with `chunk_size = 500`, `chunk_overlap = 50`.
- Small chunks missed context, large chunks returned off-topic results.

---

## 💭 Reflection

Building this RAG system taught me how search + generation can be combined. I now understand how AI agents retrieve and summarize info in real time. I also saw how things like embedding models, chunking, and index types affect results. Most importantly, I learned to debug deep dependency issues with real tools and Python packages.

