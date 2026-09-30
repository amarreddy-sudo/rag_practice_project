def rerank(query: str, documents: list[str], top_n: int = 3) -> list[str]:
    """Demo lexical reranker.

    Production systems may use a cross-encoder reranker.
    """
    query_terms = set(query.lower().split())

    scored = []
    for document in documents:
        terms = set(document.lower().split())
        score = len(query_terms.intersection(terms))
        scored.append((score, document))

    scored.sort(reverse=True, key=lambda item: item[0])
    return [document for _, document in scored[:top_n]]
