from contextlib import chdir
from pathlib import Path

from asynctor import Shell

BASE_DIR = Path(__file__).parent.resolve().parent


def _run_test(d: Path) -> None:
    print(f"--> cd {d.relative_to(BASE_DIR)}")
    with chdir(d):
        rc = Shell("pytest").call(verbose=True)
        if rc != 0:
            raise SystemExit(rc)


def main() -> None:
    test_dir = BASE_DIR / "tests"
    for d in test_dir.glob("*"):
        if d.is_dir():
            _run_test(d)


if __name__ == "__main__":
    main()
