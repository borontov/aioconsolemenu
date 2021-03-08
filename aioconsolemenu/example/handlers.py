"""Item handlers."""
from time import sleep

from aioconsole import aprint

from aioconsolemenu.actions import ExitAction, SwitchMenuAction
from aioconsolemenu.menu import Menu


async def first_item_handler(current_menu: Menu) -> None:
    """Handler for first item."""
    next_action = ExitAction()
    current_menu.asyncio_gather.set_result(next_action)  # type: ignore
    current_menu.asyncio_gather.done()


async def second_item_handler(current_menu: Menu) -> None:
    """Handler for second item."""
    from aioconsolemenu.example.main import sub_menu  # noqa: WPS433

    next_action = SwitchMenuAction(current_menu=current_menu, next_menu=sub_menu)
    current_menu.asyncio_gather.set_result(next_action)  # type: ignore
    current_menu.asyncio_gather.done()


async def other_items_handler(current_menu: Menu) -> None:
    """Handler for other items."""
    await aprint("other items handler")
    sleep(1)


async def submenu_exit_handler(current_menu: Menu) -> None:
    """Handler for other items."""
    from aioconsolemenu.example.main import main_menu  # noqa: WPS433

    next_action = SwitchMenuAction(current_menu=current_menu, next_menu=main_menu)
    current_menu.asyncio_gather.set_result(next_action)  # type: ignore
    current_menu.asyncio_gather.done()
