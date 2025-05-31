import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import logging
from transformers import logging as hf_logging
import warnings

# Suppress unnecessary Logs
logging.getLogger("langchain.text_splitter").setLevel(logging.ERROR)
hf_logging.set_verbosity_error()
warnings.filterwarnings("ignore")

# Config
chunk_size = 500
chunk_overlap = 50
model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"
top_k = 5

# Load text
with open("Selected_Document.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Chunk text
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
chunks = text_splitter.split_text(text)

# Generate embeddings
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

embedder = SentenceTransformer("paraphrase-MiniLM-L6-v2")
embeddings = embedder.encode(chunks, show_progress_bar=True)
embedding_array = np.array(embeddings).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(embedding_array.shape[1])
index.add(embedding_array)

# Load text generation model
from transformers import pipeline
generator = pipeline("text2text-generation", model="google/flan-t5-small", device=-1)

# Retrieval function
def retrieve_chunks(question, k=top_k):
    question_embedding = embedder.encode([question]).astype("float32")
    distances, indices = index.search(question_embedding, k)
    return [chunks[i] for i in indices[0]]

# QA generation
def answer_question(question):
    context_chunks = retrieve_chunks(question)
    context = "\n".join(context_chunks)
    prompt = f"Use the context to answer the question. \nContext:\n{context}\nQuestion: {question}"
    result = generator(prompt, max_length=256, do_sample=False)[0]['generated_text']
    return result

# Interactive Q&A Loop
if __name__ == "__main__":
    print("Enter 'exit' or 'quit' to end.")
    while True:
        question = input("Your question: ")
        if question.lower() in ("exit", "quit"):
            break
        print("Answer:", answer_question(question))
    

