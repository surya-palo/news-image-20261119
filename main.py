"""news-image-20261119 entry: copy the pre-rendered poster to /output/entry.png.

Standard library only. Deterministic: the same bytes are copied every run.
The copy is verified byte-for-byte (SHA-256) so a truncated or partial
write fails loudly instead of submitting a corrupt image.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import hashlib
import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


DST.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
if _sha256(SRC) != _sha256(DST):
    raise SystemExit("entry.png copy failed verification")
