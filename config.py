import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

PACK_DIR = BASE_DIR / "research_pack"
SYSTEM_PROMPT = BASE_DIR / "system_prompt.md"