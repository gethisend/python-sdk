# Python SDK guidance

This independent repository publishes `hisend`. Supported Python versions and
dependencies are declared in `pyproject.toml` (currently Python >=3.7 and
`requests`). Do not introduce syntax/APIs beyond that minimum without an
explicit compatibility decision.

- `hisend/client.py`: HTTP session and resources.
- `hisend/models.py`: request/response models.
- `hisend/webhooks.py`: signature verification.
- `hisend/__init__.py`: public exports.

Run `python -m unittest discover -s tests -v` using the intended environment.
If dependencies are missing, install into a virtual environment, not system
Python (`python -m pip install -e .` inside that environment when needed).
Tests mock `requests.Session.request`; follow that pattern and never call the
live default endpoint for verification.

Preserve public exports, Python compatibility, JSON contracts, error handling,
and webhook security. Check related backend/SDK docs when present. Do not edit
`dist/`, `*.egg-info`, or `__pycache__` directly or treat packaged releases as
source. Do not change versions or upload packages without request.
