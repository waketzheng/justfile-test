from pathlib import Path

from src_project import __version__


def test_version():
    file = Path(__file__).parent.resolve().parent / "src/src_project/__init__.py"
    text = file.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    v = "__version__"
    version_line = next(i for i in lines if i.startswith(v))
    value = version_line.split("=", 1)[-1].split("#")[0].strip().strip("'\"")
    assert value == __version__
