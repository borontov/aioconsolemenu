"""Item handlers."""
from time import sleep
from typing import Any

from aioconsole import aprint


async def first_item_handler(self: Any) -> None:
    """Handler for first item."""
    self.loops.set_result(("exit",))  # type: ignore
    self.loops.done()


async def second_item_handler(self: Any) -> None:
    """Handler for second item."""
    from aioconsolemenu.example.main import second_menu  # noqa: WPS433

    self.loops.set_result(("switch_asyncio_gather", second_menu.start))  # type: ignore
    self.loops.done()


async def other_items_handler(self: Any) -> None:
    """Handler for other items."""
    await aprint("other items handler")
    sleep(3)
