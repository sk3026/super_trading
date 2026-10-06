# Super Investing - AI Research Agent

An AI research agent that analyzes a company using a supplied set of research documents and generates a concise investment research brief.

## Target Company

Ticker:

SRVCABLE

Company:

Sarvottam Cables Ltd

## Architecture

The agent uses a two-pass research workflow:

Research Documents
        |
        v
    loader.py
        |
        v
Evidence Extraction
        |
        v
  evidence.txt
        |
        v
Research Brief Generation
        |
        v
    brief.md
        |
        v
   validator.py

## Project Structure

```text
super_investing_agent/
│
├── research_pack/
├── .env
├── .gitignore
│
├── agent.py
├── config.py
├── loader.py
├── prompts.py
├── llm.py
├── validator.py
│
├── system_prompt.md
├── evidence.txt
├── brief.md
├── README.md
└── requirements.txt