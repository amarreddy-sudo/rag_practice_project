from app.retrieval import retrieve


def test_retrieve_returns_top_k():
    documents = [
        "RAG uses retrieval.",
        "Python is a programming language.",
        "Embeddings represent text as vectors.",
    ]

    result = retrieve("RAG retrieval", documents, top_k=2)

    assert len(result) == 2
