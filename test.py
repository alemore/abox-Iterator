from boxes.svgmerge import SvgMerge
from pathlib import Path
import glob

files = list(Path("test").glob("*.svg"))



merger = SvgMerge()
merger.parseArgs([
    "--panel_width", "1200",
    "--pack_algo", "MaxRectsBaf",
    "--bin_algo", "Global",
    "--panel_height", "600",
    "--margin", "1",
    "--rotation",
    "--output", "nested.svg",
] + [str(f) for f in files])

merger.render([str(f) for f in files])
data = merger.close()

with open("nested.svg", "wb") as f:
    f.write(data.getvalue())