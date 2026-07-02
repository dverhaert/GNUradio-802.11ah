#!/usr/bin/env python3
"""Fast non-hardware smoke checks for this repository.

This script intentionally avoids importing GNU Radio so it can run in CI without SDR deps.
"""

from __future__ import annotations

import pathlib
import sys
import xml.etree.ElementTree as ET

REPO = pathlib.Path(__file__).resolve().parents[1]
GRC_FILES = [
    REPO / "802_11_ah_rx.grc",
    REPO / "802_11_ah_tx.grc",
    REPO / "802_11_ah_txrx.grc",
    REPO / "basictest.grc",
]
PY_FILES = [
    REPO / "basictest.py",
    REPO / "top_block.py",
    REPO / "transceiver_802_11_ah.py",
]


def check_grc_xml() -> list[str]:
    errors = []
    for path in GRC_FILES:
        if not path.exists():
            errors.append("missing file: {}".format(path.name))
            continue
        try:
            ET.parse(str(path))
        except ET.ParseError as exc:
            errors.append("invalid XML in {}: {}".format(path.name, exc))
    return errors


def check_legacy_python_markers() -> list[str]:
    errors = []
    for path in PY_FILES:
        if not path.exists():
            errors.append("missing file: {}".format(path.name))
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        if "#!/usr/bin/env python2" not in content:
            errors.append("{}: expected legacy shebang not found".format(path.name))
    return errors


def main() -> int:
    errors = []
    errors.extend(check_grc_xml())
    errors.extend(check_legacy_python_markers())

    if errors:
        print("SMOKE CHECK FAILED")
        for err in errors:
            print("- {}".format(err))
        return 1

    print("SMOKE CHECK PASSED")
    print("- GRC XML files parse correctly")
    print("- Legacy Python script markers are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
