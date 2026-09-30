from .chunking import chunk_text
from .retrieval import retrieve
from .reranker import rerank
from .llm import generate_answer


DOCUMENTS = [
    "RAG combines retrieval with generation to improve answers using external knowledge.",
    "Embeddings convert text into vectors that can be compared for semantic similarity.",
    "A reranker can reorder retrieved documents before sending context to an LLM.",
    "Hybrid retrieval can combine vector search and keyword search.",
]


def answer_question(query: str) -> str:
    all_text = "\n".join(DOCUMENTS)
    chunks = chunk_text(all_text, chunk_size=180, overlap=20)

    retrieved = retrieve(query, chunks, top_k=5)
    reranked = rerank(query, retrieved, top_n=3)

    return generate_answer(query, reranked)


if __name__ == "__main__":
    print(answer_question("What is the purpose of a reranker in RAG?"))
