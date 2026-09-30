def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Create simple overlapping text chunks."""
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks
