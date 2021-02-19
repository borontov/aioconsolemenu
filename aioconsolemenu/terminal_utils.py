"""Utils for work with terminal."""
import os


def clear_terminal() -> None:
    """Clear display of terminal."""
    os.system("cls" if os.name == "nt" else "clear")  # noqa: S605
