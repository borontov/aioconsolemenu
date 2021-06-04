"""Demo asyncio code."""

from aioconsolemenu.example.items import items1, items2
from aioconsolemenu.manager import AsyncMenuManager
from aioconsolemenu.menu import Menu

on_press = print
main_menu = Menu(items1, on_press=on_press, items_per_page=4, title="Menu without pagination")
sub_menu = Menu(items2, on_press=on_press, items_per_page=6, title="Submenu with pagination")


def start_demo() -> None:
    """Asyncio logic for start main_menu and handle gather results on done."""
    menu_manager = AsyncMenuManager(start_menu=main_menu)
    menu_manager.run()
