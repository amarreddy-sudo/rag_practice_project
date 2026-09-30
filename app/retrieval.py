from .embeddings import embed_text


def similarity(a: list[float], b: list[float]) -> float:
    """Simple demo similarity score."""
    return 1.0 / (1.0 + abs(a[0] - b[0]) + abs(a[1] - b[1]))


def retrieve(query: str, documents: list[str], top_k: int = 5) -> list[str]:
    query_vector = embed_text(query)

    scored = [
        (similarity(query_vector, embed_text(document)), document)
        for document in documents
    ]

    scored.sort(reverse=True, key=lambda item: item[0])
    return [document for _, document in scored[:top_k]]
