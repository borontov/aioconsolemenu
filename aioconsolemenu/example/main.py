"""Demo asyncio code."""
import asyncio
from typing import Any, Optional

from aioconsolemenu.example.items import items1, items2
from aioconsolemenu.example.menus import MyCustomMenu
from aioconsolemenu.terminal_utils import clear_terminal

main_menu = MyCustomMenu(items=items1, items_per_page=4, title="Main menu")

second_menu = MyCustomMenu(
    items=items2,
    items_per_page=6,
    title="Second Menu",
)


def actions_handler(
    loop: asyncio.AbstractEventLoop,
    action: Optional[str],
    arg: Any,
) -> Optional[bool]:
    """Handler for asyncio.gather results."""
    if action == "exit":
        return True
    elif action == "switch_asyncio_gather":
        loop.run_until_complete(arg())
        return False
    else:
        print("Unexpected action. Please, fix it. The application will be closed.")
        return True


def start_demo() -> None:
    """Asyncio logic for start main_menu and handle gather results on done."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_menu.start())
    while True:
        result = main_menu.loops.result()

        action = result[0]
        try:
            arg = result[1]
        except IndexError:
            arg = None

        exit_request = actions_handler(loop, action, arg)
        if exit_request:
            clear_terminal()
            break
