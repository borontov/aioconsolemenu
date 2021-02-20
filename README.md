# aioconsolemenu

A module that allows you to create console menus using asyncio coroutines to embed asynchronous events such as real-time updating of menu items.

## Table of Contents
- [Features](#features)
- [Basic Usage](#basic-usage)
- [FAQ](#faq)
    - [Terminal is flickering. How to fix it?](#terminal-is-flickering-how-to-fix-it)
    - [Why should I write my own asyncio loops and input handlers logic?](#why-should-i-write-my-own-asyncio-loops-and-input-handlers-logic)

## Features

- Menu items can be sorted using sort_id, but by default they are sorted by title.
- You can update menu items in real time.
- You can write your own handler for user input and for item selection. Or use it from demo example.
- You can change the output printing templates.
- You can terminate or not terminate the menu loop when you select a menu item.
- You can return to the top level menu by stopping the submenu loop and starting the top level menu loop.

## Basic Usage

First, you must create a class that inherits from the Menu class. You will need to create a user input handler. You can see an example in the example folder.

```python
from aioconsolemenu import templates
from aioconsolemenu.menu import Menu

class MyCustomMenu(Menu):
    """Custom menu for demo."""

    async def input_handler(self, input_text: str) -> None:
        """Custom input handler."""
        select = int(input_text)
        item_id = select - 1

        if self.paginator:
            target_list = self.paginator.current_page_items
        else:
            target_list = self.items

        if select > len(target_list):
            print(templates.SELECT_OUT_OF_AVAILABLE_OPTIONS.render())
        else:
            await target_list[item_id]["callback"](self)

```

Then you have to create menu items and asynchronous handlers for them. If you specify sort_id, then items with sort_id in ascending order are printed first. After that, items without sort_id are printed.

```python
async def first_item_handler(self: Any) -> None:
    """Handler for first item."""
    self.loops.set_result(("exit",))  # type: ignore
    self.loops.done()


async def second_item_handler(self: Any) -> None:
    """Handler for second item."""
    from aioconsolemenu.example.main import second_menu

    self.loops.set_result(("switch_asyncio_gather", second_menu.start))
    self.loops.done()


async def other_items_handler(self: Any) -> None:
    """Handler for other items."""
    await aprint("other items handler")

items1 = Items()
items1.add("Second item", callback=second_item_handler, sort_id=5)
items1.add("4-h item", callback=other_items_handler)
items1.add("3-h item", callback=other_items_handler)
items1.add("First item", callback=first_item_handler, sort_id=3)
```

Now you can instantiate your custom menu class.

```python
main_menu = MyCustomMenu(items=items1, items_per_page=4, title="Main menu")

second_menu = MyCustomMenu(
    items=items2,
    items_per_page=6,
    title="Second Menu",
)
```

To start the menu you need to pass your_menu.start() coroutine to the asyncio loop. To stop the menu loops, call your_menu.loops.set_result(). All menu cycles are terminated if the gather of this menu has a result. We did this earlier in first_item_handler and second_item_handler. Here we write the gather result handlers:

```python
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
```


## FAQ

### Terminal is flickering. How to fix it?
Try specifying screen_redraw_rate_in_seconds when instantiating the menu class. If this does not work, then try running the script in a different terminal emulator.

### Why should I write my own asyncio loops and input handlers logic?
I figured it's best not to hardcode things that might not be suitable for a wide range of tasks.
