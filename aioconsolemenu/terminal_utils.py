"""Utils for work with terminal."""
import os


def terminal_clear() -> None:
    """Clear display of terminal."""
    os.system("cls" if os.name == "nt" else "clear")  # noqa: S605
