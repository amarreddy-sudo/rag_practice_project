def generate_answer(query: str, context: list[str]) -> str:
    """Demo LLM layer.

    Replace this with your actual LLM provider in a real project.
    """
    context_text = "\n".join(context)

    return (
        f"Question: {query}\n\n"
        f"Retrieved context:\n{context_text}\n\n"
        "Demo answer generated from retrieved context."
    )
