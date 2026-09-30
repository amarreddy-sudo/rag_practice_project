from pathlib import Path


def load_document(path: str) -> str:
    """Load a text document from disk."""
    return Path(path).read_text(encoding="utf-8")
