# LLM choice (locked for main runs)

| Field | Value |
|-------|--------|
| Backend | **Ollama (local)** |
| Model | `llama3.2:3b` |
| Why | No API key; reproducible; M4 Pro / Metal; ~2 GB download |
| Installed | 2026-08-04 |
| CLI | `~/.local/bin/ollama` → `/Applications/Ollama.app/Contents/Resources/ollama` |
| API | `http://127.0.0.1:11434` |

## How to run

1. Open **Ollama.app** once (menu bar icon) — or it may already be running.  
2. Test: `export PATH="$HOME/.local/bin:$PATH"` then `ollama list`  
3. Annotate via API with `temperature: 0` in project notebooks.

## Project framing

Scientific focus: **linguistic loci of disagreement** in literary DE/EN (not model bake-off).  
Annotators: SpaCy + this Ollama model as instruments.


## Smoke test (2026-08-04)

- One DE sentence (`sent_id=26`, 23 tokens) via `src.ollama_client.annotate_tokens`
- Raw cache: `data/processed/llm_cache/_smoke_de.json`
- Rough UPOS agreement vs SpaCy on that sentence: **52%** (expected to be noisy for a 3B model; full sample comes in Phase 3)

## Leaving it running

Yes. Keep **Ollama.app** open (or its background service). Idle models unload from RAM automatically; the server stays up. For long overnight annotation jobs, prevent Mac sleep (or use `caffeinate`).
