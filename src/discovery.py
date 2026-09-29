"""Deterministic product discovery engine used by the MVP demo."""


def generate_discovery(product_idea: str) -> dict:
    """Turn a product idea into a small, reviewable discovery package.

    The deterministic baseline makes the project runnable without an API key.
    An AI provider can be added later behind the same result shape.
    """
    idea = product_idea.strip()
    if not idea:
        raise ValueError("product idea must not be empty")

    return {
        "problem_statement": (
            f"Users need a simpler way to solve the problem represented by: {idea}."
        ),
        "hypotheses": [
            "The target user experiences the problem frequently enough to seek a solution.",
            "A focused MVP can reduce effort or uncertainty in the current workflow.",
            "Users will return if the first value is delivered in the initial session.",
        ],
        "user_stories": [
            {
                "title": "Describe the current problem",
                "story": "As a target user, I want to describe my current workflow so that the product can focus on my real need.",
                "acceptance_criteria": [
                    "The user can submit a non-empty problem description.",
                    "The submitted description is displayed in the discovery result.",
                ],
            },
            {
                "title": "See a first actionable result",
                "story": "As a target user, I want a concise first result so that I can decide whether the MVP is useful.",
                "acceptance_criteria": [
                    "The result contains a problem statement.",
                    "The result contains at least two testable hypotheses.",
                ],
            },
            {
                "title": "Review the MVP scope",
                "story": "As a product owner, I want a prioritized backlog so that the team can deliver the smallest useful release.",
                "acceptance_criteria": [
                    "The backlog contains Must have and Should have items.",
                    "Each item includes a reason for its priority.",
                ],
            },
        ],
        "backlog": [
            {
                "title": "Capture the core problem",
                "priority": "Must have",
                "reason": "Without a clear problem, discovery cannot be evaluated.",
            },
            {
                "title": "Generate a first actionable result",
                "priority": "Must have",
                "reason": "The first user session must deliver observable value.",
            },
            {
                "title": "Add AI provider integration",
                "priority": "Should have",
                "reason": "The deterministic baseline works first; AI enrichment can follow.",
            },
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(generate_discovery("Uma plataforma para organizar entregas"), indent=2))
