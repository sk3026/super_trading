from pathlib import Path


def load_documents(pack_dir: Path):
    documents = []

    files = sorted(pack_dir.glob("*.md"))

    for i, file in enumerate(files, 1):
        text = file.read_text(encoding="utf-8")

        documents.append({
            "id": f"S{i}",
            "file": file.name,
            "text": text
        })

    return documents