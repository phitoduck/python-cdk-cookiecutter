# python-cdk-cookiecutter

An opinionated template for working with AWS CDK and Python.

Opinions:

- Monorepo with 2-boilerplate packages; can be extended to any number
- Editor support: pre-configured for VS Code, specifically a multi-root workspace
- Deployed with GitHub Actions
- Justfile as a task runner (as opposed to Makefile and others)
- Pydantic for a settings file
- `pre-commit` Framework
- Testing: `pytest`
- Formatting: `Black`, `isort`
- Linting: `flake8`, `pylint`, `mypy`
- Packaging: setuptools and `pyproject.toml`
- Versioning: Semantic versioning; manually bump `VERSION.txt` before merging
- Documentation: README and docstrings all use Markdown (as opposed to reStructuredText)