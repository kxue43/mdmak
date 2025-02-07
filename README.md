# mdmak

`mdmak` is a Python CLI program that converts a Markdown file to a GitHub style HTML.

Example invocation is:

```bash
mdmak /path/to/input.md /path/to/output.html
```

## Setup Project

Install `pyenv` and `poetry>=2.0.1` first.

```bash
pyenv local 3.11
poetry env use $(pyenv which python)
poetry install
```

## Make a Release

```bash
eval $(poetry env activate)
python -m build
export MDMAK_VERSION=$(poetry version --short)
gh release create $MDMAK_VERSION --latest dist/mdmak-${MDMAK_VERSION}-py3-none-any.whl
```

## Install from GitHub Release Asset

Users of this package can conveniently install it from the wheel file available as GitHub release asset.
This package is not on PyPI.

```bash
pip install "mdmak@https://github.com/kxue43/mdmak/releases/download/1.0.0/mdmak-1.0.0-py3-none-any.whl"
```
