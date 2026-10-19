"""Build Calcure as a standalone, single-file executable."""

from pathlib import Path
import sys

from PyInstaller.__main__ import run


ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "calcure" / "builder"


def main() -> None:
    executable_name = "calcure"
    if sys.platform == "win32":
        executable_name += ".exe"

    run(
        [
            "--onefile",
            "--console",
            "--clean",
            "--noconfirm",
            "--name",
            executable_name,
            "--distpath",
            str(ROOT / "calcure"),
            "--workpath",
            str(BUILDER / "build"),
            "--specpath",
            str(BUILDER),
            "--paths",
            str(ROOT),
            "--collect-all",
            "holidays",
            "--collect-all",
            "icalendar",
            str(ROOT / "calcure" / "__main__.py"),
        ]
    )


if __name__ == "__main__":
    main()
