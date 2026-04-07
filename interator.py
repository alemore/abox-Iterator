import os
import subprocess
from itertools import product
from pathlib import Path
from boxes.generators.abox import ABox


boxes_py = "boxes/boxes/scripts/boxes_main.py"
output_dir = "output"

# os.makedirs(output_dir, exist_ok=True)

fixed_params = {
    "FingerJoint_style": "rectangular",
    "FingerJoint_surroundingspaces": 2.0,
    "FingerJoint_bottom_lip": 0.0,
    "FingerJoint_edge_width": 1.0,
    "FingerJoint_extra_length": 0.0,
    "FingerJoint_finger": 6,
    "FingerJoint_play": 0.0,
    "FingerJoint_space": 6,
    "FingerJoint_width": 1.0,

    "Lid_handle": "none",
    "Lid_style": "none",
    "Lid_handle_height": 8.0,
    "Lid_height": 4.0,
    "Lid_play": 0.1,

    "outside": 1,
    "bottom_edge": "F",

    "format": "svg",
    "tabs": 0.0,
    "qr_code": 0,
    "debug": 0,
    "labels": 1,

    "reference": 0,
    "inner_corners": "loop",
    "burn": 0.06,
    "spacing": 0.5
}

clearance = 0.5

unit_x = 42
unit_y = 42
unit_h = 7
lip_h = 3.8 

x =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
h = [7, 9, 14]
thicknesses = [2.5,2.75,3,3.25,3.5]


for xi, yi, hi, thk in product(x, y, h, thicknesses):
    if xi <= yi:
        xs = (unit_x * xi) - clearance
        ys = (unit_y * yi) - clearance
        hs = (unit_h * hi) + lip_h

        print (f"{xi} x {yi} x {hi} x {thk}mm")

        thickness_dir = Path("output") / f"{thk:.2f} mm"
        thickness_dir.mkdir(parents=True, exist_ok=True)

        out = thickness_dir / f"gridfinity_{xi}x{yi}x{hi}_thk_{thk}.svg"

        # param_args = [f"--{k}={v}" for k, v in fixed_params.items()]
        param_args = []
        for k, v in fixed_params.items():
            param_args.extend([f"--{k}", str(v)])

        box = ABox()
        box.parseArgs( param_args + [
            "--x", str(xs),
            "--y", str(ys),
            "--h", str(hs),
            "--thickness", str(thk),
        ])
        box.open()
        box.render()
        data = box.close()

        with open(out, "wb") as f:
            f.write(data.getvalue())