import re


def validate(brief, documents):

    errors = []

    required_sections = [
        "## Snapshot",
        "## Bull case",
        "## Bear case",
        "## Open questions",
        "## Sources"
    ]

    # Check required sections
    for section in required_sections:
        if section not in brief:
            errors.append(f"Missing section: {section}")

    # Valid source IDs
    valid_sources = {
        document["id"]
        for document in documents
    }

    # Find source tags such as [S1], [S2]
    used_sources = set(
        re.findall(r"\[(S\d+)\]", brief)
    )

    invalid_sources = used_sources - valid_sources

    if invalid_sources:
        errors.append(
            f"Invalid source references: {invalid_sources}"
        )

    # Check that at least one source is used
    if not used_sources:
        errors.append(
            "No source references found."
        )

    return errors