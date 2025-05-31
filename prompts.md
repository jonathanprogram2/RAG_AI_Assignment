# prompts.md

## AI Prompts Used to Generate Code

### requirements.txt
> Generate a requirements.txt listing exactly these seven libraries (one per line): beautifulsoup4, langchain, sentence-transformers, numpy, faiss-cpu, transformers, torch

---

### text_extractor.py (Wikipedia)
> Write a Python function called scrape_webpage(url) that uses requests to fetch the Wikipedia page, parses it with BeautifulSoup, extracts all <p> tags inside <div class='mw-parser-output'>, joins their text with blank lines, writes the result to Selected_Document.txt (UTF‑8), prints a success/failure message based on the HTTP status code, and returns the article text. Include a main() function and if __name__ == '__main__': block.

---

### RAG_app.py

**Suppress Logs**  
> Write code to import logging, transformers.logging (as hf_logging), and warnings; then set log levels of langchain.text_splitter and transformers to ERROR, and filter Python warnings.

**Chunking Config**  
> Write code to define chunk_size = 500, chunk_overlap = 50, model_name, and top_k.

**Read Text**  
> Write code to open Selected_Document.txt in UTF-8 mode and read contents into a variable.

**Split Chunks**  
> Use RecursiveCharacterTextSplitter with separators and chunk size/overlap to split text into chunks.

**Embed + FAISS**  
> Load SentenceTransformer, encode chunks, store embeddings in a FAISS index.

**Load Generator**  
> Set up a HuggingFace pipeline('text2text-generation', model='google/flan-t5-small', device=-1)

**Retrieve + Answer Functions**  
> Define retrieve_chunks() to return top-k results, and answer_question() to call generator with context and return the result.

**Interactive Loop**  
> Create an input() loop that allows questions until user types 'exit' or 'quit'
