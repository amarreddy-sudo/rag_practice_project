def embed_text(text: str) -> list[float]:
    """Tiny deterministic demo embedding.

    A real project would call an embedding model such as a
    Sentence Transformers, BGE, E5, or API-based embedding model.
    """
    return [float(len(text)), float(sum(ord(c) for c in text) % 1000)]
