# Builtin
from pathlib import Path
import re
import sys

# External
from marko.ext.gfm import gfm


PLACEHOLDER = re.compile(r"BODY_PLACEHOLDER")


def main() -> None:
    """
    Example CLI invocation:

    .. code-block:: bash

       $ mdmak /path/to/input.md /path/to/output.html
    """
    template_path = Path(__file__).parent.joinpath("template", "github_style.html")
    inpath = Path(sys.argv[1])
    outpath = Path(sys.argv[2])
    with open(inpath, "r") as fr:
        markdown_input = fr.read()
    with open(template_path, "r") as fr:
        html_template = fr.read()
    with open(outpath, "w") as fw:
        fw.write(PLACEHOLDER.sub(gfm(markdown_input), html_template))
