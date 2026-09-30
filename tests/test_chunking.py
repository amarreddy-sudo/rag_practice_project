from app.chunking import chunk_text


def test_chunking_returns_chunks():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunks = chunk_text(text, chunk_size=10, overlap=2)

    assert len(chunks) > 1
    assert chunks[0] == "abcdefghij"
