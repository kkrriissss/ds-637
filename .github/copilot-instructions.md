## Quick orientation for AI coding agents

This repository is a small teaching/demo Python workspace for DS-637. It contains notebooks and a few simple Python scripts. The goal of these instructions is to highlight project-specific patterns and where to find the most relevant code so an AI coding agent can be immediately productive.

Key locations
- `README.md` — minimal project README (top-level). Use it to confirm repository purpose.
- `week1/` — contains Jupyter notebooks (course materials). Example: `week1/1. Python Basics.ipynb`.
- `week2/` — lightweight Python scripts for in-class examples. Example: `week2/inclass.py` (currently empty placeholder).
- `test/` — contains `test.ipynb` (not a unit-test folder; it's a notebook).

Big-picture architecture
- This is not a packaged application or service. It's a collection of teaching notebooks and small scripts. There are no modules, packages, or services to wire together.
- Treat notebooks (`.ipynb`) as the primary source of executable logic and examples. Scripts under `week2/` are supporting class/demo code.

Project-specific conventions
- Notebooks contain the learning content. When asked to add runnable code, prefer adding a new `.py` module under `week2/` or a new notebook in `test/` that demonstrates usage, and keep the changes minimal and focused.
- Keep single-file edits small. Avoid introducing new heavy dependencies without adding a `requirements.txt` or noting installation steps.

Build, test, and debugging notes
- There is no build system or tests configured. To run notebooks interactively use your local Jupyter environment. For quick script checks, run:

```powershell
python .\\week2\\inclass.py
```

- If adding dependencies, update the repo root with a `requirements.txt` and include a short note in `README.md` on how to create a virtual environment and install them.

Integration points and external dependencies
- There are no external APIs, services, or CI configurations discoverable in the repository. Assume standalone, offline code unless the user specifies otherwise.

Examples to reference when making changes
- Add small runnable examples as standalone Python scripts in `week2/` and, when appropriate, include a short demo notebook in `test/` that imports/uses the script.
- If modifying notebooks, keep output cells minimal. Prefer adding new code cells rather than editing old cells that contain instructor outputs.

How to propose changes in PRs
- Provide a short summary that explains why the change is needed for teaching/demo purposes.
- If adding packages, include `requirements.txt`, update `README.md` with install/run instructions, and keep the scope small.

If something is missing
- Ask the repo owner which notebook(s) represent canonical exercises and whether they prefer scripts or notebooks for new examples.

Files referenced by these instructions
- `README.md`
- `week1/1. Python Basics.ipynb`
- `week2/inclass.py`
- `test/test.ipynb`

Feedback
- Please review this guidance and tell me what should be expanded (for example: preferred Python version, virtualenv vs conda, or a style guide).
