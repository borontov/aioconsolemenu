import asyncio
from asyncio import AbstractEventLoop
from time import sleep
from typing import Any, Optional

from aioconsole import aprint

from aioconsolemenu.items import Items
from aioconsolemenu.menu import Menu
from aioconsolemenu.terminal_utils import terminal_clear


async def first_item_handler(self: Any) -> None:
    await aprint("async action")
    await asyncio.sleep(3)
    print("hello!")
    sleep(2)
    self.loops.set_result(("exit",))  # type: ignore
    self.loops.done()


async def second_item_handler(self: Any) -> None:
    print("second handler!")
    self.loops.set_result(("switch_asyncio_gather", second_menu.start))  # type: ignore
    self.loops.done()


async def universal_handler(self: Any) -> None:
    print("unversal handler!")
    sleep(2)


items1 = Items()
items1.add("Second item", callback=second_item_handler, sort_id=5)
items1.add("4-h item", callback=universal_handler)
items1.add("3-h item", callback=universal_handler)
items1.add("First item", callback=first_item_handler, sort_id=3)
items1.add("5-h item", callback=universal_handler)
items1.add("6-h item", callback=universal_handler)
items1.add("7-h item", callback=universal_handler)
items1.add("8-h item", callback=universal_handler)
items1.add("9-h item", callback=universal_handler)
items1.add("91-h item", callback=universal_handler)
items1.add("92-h item", callback=universal_handler)
items2 = Items(range(200, 400))


class MainMenu(Menu):
    async def input_handler(self, input_text: str) -> None:
        select = int(input_text)
        if self.paginator:
            if select > len(self.paginator.current_page_items):
                print("There is no such menu item")
            else:
                await self.paginator.current_page_items[select - 1]["callback"](self)
        else:
            if select > len(self.items):
                print("There is no such menu item")
            else:
                await self.items[select - 1]["callback"](self)


class SecondMenu(Menu):
    async def input_handler(self, input_text: str) -> None:
        select = int(input_text)
        if self.paginator:
            if select > len(self.paginator.current_page_items):
                print("There is no such menu item")
            else:
                try:
                    await self.paginator.current_page_items[select - 1]["callback"](
                        self
                    )
                except Exception:
                    exit()
        else:
            if select > len(self.items):
                print("There is no such menu item")
            else:
                await self.items[select - 1]["callback"](self)


main_menu = MainMenu(items=items1, items_per_page=4, title="Main menu")

second_menu = SecondMenu(
    items=items2,
    items_per_page=6,
    title="Second Menu",
)


def actions_handler(loop: AbstractEventLoop, action: str, arg: Any) -> Optional[bool]:
    if action == "exit":
        return True
    elif action == "switch_asyncio_gather":
        loop.run_until_complete(arg())
    else:
        print("Unexpected action. Please, fix it. The application will be closed.")
        return True


def start_demo() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_menu.start())
    while True:
        result = main_menu.loops.result()
        action = result[0]
        try:
            arg = result[1]
        except IndexError:
            arg = None
        exit = actions_handler(loop, action, arg)
        if exit:
            terminal_clear()
            break
