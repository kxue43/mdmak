# `mdmak` CLI

## Setup Project

```bash
pyenv local 3.11
poetry env use $(pyenv which python)
poetry install
```

## Build Wheel

```bash
eval $(poetry env activate)
python -m build
```

## Install on macOS

```bash
/usr/bin/python3 -m pip install /PATH/TO/mdmak/dist/mdmak-1.0.0-py3-none-any.whl
```

## Get CLI Absolute Path

```bash
echo "$(/usr/bin/python3 -c 'import site; print(site.getuserbase());')/bin/mdmak"
```
