"""Local (untracked) config for external executables.

How to use:
1) Copy this file to `external_apps.py` (same folder as convert_3ds.py).
2) Edit the paths below to match your machine.

`external_apps.py` is intentionally git-ignored.

Notes:
- You can set a full path (recommended on Windows), or just a command name if it's on PATH.
- Inkscape is used to export SVG layers to PNGs.
- tex3ds is used only for the 3DS target to build .t3x from .t3s.
"""

# Inkscape executable.
# Example Windows install path:
# Prefer the CLI-friendly binary when available (often `inkscape.com`).
INKSCAPE_PATH = r"/bin/inkscape"

# tex3ds executable (devkitPro tools).
# Example Windows install path:
TEX3DS_PATH = r"/home/ubuntu/bin/tex3ds"
