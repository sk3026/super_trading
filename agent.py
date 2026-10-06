from config import PACK_DIR, SYSTEM_PROMPT
from loader import load_documents
from prompts import evidence_prompt, brief_prompt
from llm import ask
from validator import validate


def main():

    ticker = "SRVCABLE"

    print("Loading research documents...")

    documents = load_documents(PACK_DIR)

    if not documents:
        print("No research documents found.")
        return

    print(f"Loaded {len(documents)} documents.")

    # Load system prompt
    system = SYSTEM_PROMPT.read_text(
        encoding="utf-8"
    )

    # -------------------------------------------------
    # PASS 1: Evidence extraction
    # -------------------------------------------------

    print("\nExtracting evidence...")

    evidence = ask(
        system,
        evidence_prompt(ticker, documents)
    )

    with open(
        "evidence.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(evidence)

    print("Evidence saved to evidence.txt")

    # -------------------------------------------------
    # PASS 2: Research brief generation
    # -------------------------------------------------

    print("\nGenerating research brief...")

    brief = ask(
        system,
        brief_prompt(
            ticker,
            evidence,
            documents
        )
    )

    with open(
        "brief.md",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(brief)

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    errors = validate(
        brief,
        documents
    )

    print("\n" + "=" * 60)
    print("GENERATED RESEARCH BRIEF")
    print("=" * 60)

    print(brief)

    print("\n" + "=" * 60)
    print("VALIDATION")
    print("=" * 60)

    if errors:

        print("Validation warnings:")

        for error in errors:
            print(f"- {error}")

    else:

        print("Validation passed.")

    print("\nFiles generated:")
    print("- evidence.txt")
    print("- brief.md")


if __name__ == "__main__":
    main()