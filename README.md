# RAG Git Practice Project

A small production-style RAG project created for learning Git and GitHub.

## Architecture

Documents -> Chunking -> Embeddings -> Retrieval -> Reranking -> LLM Answer

This demo uses simple local components so it can run without API keys.

## Project structure

- `app/` - application code
- `tests/` - tests
- `config/` - application configuration
- `.env.example` - example environment variables
- `.gitignore` - files that should not be committed
- `requirements.txt` - Python dependencies
- `Dockerfile` - container definition

## Run

```bash
python -m pip install -r requirements.txt
python -m app.main
```

## Git practice

Try this workflow:

```bash
git status
git add .
git commit -m "Initial RAG project"
git branch
git log --oneline
```

Later create a feature branch and modify `app/retrieval.py`.
