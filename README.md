# AI Product Discovery MVP

An AI-assisted product discovery workspace that turns a product idea into hypotheses, user stories, acceptance criteria, and a prioritized MVP backlog.

This portfolio project demonstrates product discovery, requirements definition, prioritization, and a deterministic baseline that runs without an API key. An AI provider can be added behind the same result shape without changing the core workflow.

## Why this project

Product teams often move from a vague idea directly to a feature list. This MVP makes the discovery step explicit and produces artifacts that a product and engineering team can review together.

## Run locally

Requires Python 3.10 or newer.

```powershell
python -m src.discovery
python -m unittest discover -s tests -v
```

The current baseline is a library and testable workflow. The next slice adds a small HTTP or Streamlit interface while preserving the deterministic core.

## Output

Given a product idea, the discovery engine returns:

- a problem statement;
- testable hypotheses;
- user stories with acceptance criteria;
- a backlog prioritized using a simple Must/Should framework.

## Responsible use

This is an independent portfolio project. It uses no employer data, proprietary code, or confidential information. AI-generated suggestions require product-owner review before implementation.

## Roadmap

- Add a Streamlit interface.
- Add an optional provider adapter for AI enrichment.
- Add WSJF scoring with transparent inputs.
- Export a discovery brief as Markdown.
