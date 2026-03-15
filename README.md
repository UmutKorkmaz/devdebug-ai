# DevDebug AI

> Multi-agent AI code review system powered by TigerData's Agentic Postgres.

## Overview

DevDebug AI is a challenge entry for the [TigerData Agentic Postgres Challenge](https://dev.to/challenges/tigerdata-2025-10-15). It uses a multi-agent architecture to perform automated code review, detect bugs, and suggest improvements — all backed by an Agentic Postgres database for persistent memory and context.

## Tech Stack

- **AI / Agents:** Multi-agent pipeline with LLM-based code analysis
- **Database:** TigerData Agentic Postgres (persistent agent memory)
- **Backend:** Python / FastAPI
- **Language:** Python

## Features

- Automated code review via AI agents
- Bug detection and fix suggestions
- Persistent agent context using Agentic Postgres
- Extensible agent pipeline architecture

## Getting Started

```bash
# Clone the repo
git clone https://github.com/UmutKorkmaz/devdebug-ai.git
cd devdebug-ai

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your TigerData and LLM API keys

# Run the app
python main.py
```

## My Role

Solo developer — designed and implemented the full multi-agent pipeline, Agentic Postgres integration, and code analysis logic as a competition submission.

## License

MIT License — see [LICENSE](LICENSE) for details.
