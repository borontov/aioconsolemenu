# aioconsolemenu

A module that allows you to create console menus using asyncio coroutines to embed asynchronous events such as real-time updating of menu items.

## Table of Contents
- [Features](#features)
- [Basic Usage](#basic-usage)
- [FAQ](#faq)
    - [Terminal is flickering. How to fix it?](#terminal-is-flickering-how-to-fix-it)

## Features

- Menu items can be sorted using sort_id, but by default they are sorted by title.
- You can update menu items in real time.
- You can write your own handler for user input and for item selection. Or use it from default Menu class.
- You can change the output printing templates.
- You can terminate the menu loop when you select a menu item by set_result() of asyncio menu gather, or not terminate.
- You can return to the top level menu by stopping the submenu asyncio gather and starting the top level menu asyncio gather.

## Basic Usage

First you have to create menu items and asynchronous handlers for them. If you specify sort_id, then items with sort_id in ascending order are printed first. After that, items without sort_id are printed.

Handlers:
```python
async def first_item_handler(current_menu: Menu) -> None:
    """Handler for first item."""
    next_action = ExitAction()
    current_menu.asyncio_gather.set_result(next_action)
    current_menu.asyncio_gather.done()


async def second_item_handler(current_menu: Menu) -> None:
    """Handler for second item."""
    next_action = SwitchMenuAction(current_menu=current_menu, next_menu=sub_menu)
    current_menu.asyncio_gather.set_result(next_action)
    current_menu.asyncio_gather.done()


async def other_items_handler(current_menu: Menu) -> None:
    """Handler for other items."""
    await aprint("other items handler")
    sleep(1)


async def submenu_exit_handler(current_menu: Menu) -> None:
    """Handler for other items."""
    next_action = SwitchMenuAction(current_menu=current_menu, next_menu=main_menu)
    current_menu.asyncio_gather.set_result(next_action)
    current_menu.asyncio_gather.done()
```

Items:
```python
items1 = Items()
items1.append(Item("Second item (submenu)", callback=second_item_handler, sort_id=5))
items1.append(Item("4-h item (print)", callback=other_items_handler))
items1.append(Item("3-h item (print)", callback=other_items_handler))
items1.append(Item("First item (exit)", callback=first_item_handler, sort_id=3))

items2 = Items()
for title in range(200, 300):
    items2.append(Item(f"{title} (print)", callback=other_items_handler))
items2.append(Item("return to main menu", callback=submenu_exit_handler, sort_id=0))
```

Now you can instantiate your custom menu class.

```python
main_menu = Menu(items1, 4, title="Menu without pagination")
sub_menu = Menu(items2, 6, title="Submenu with pagination")
```

You need to create an AsyncMenuManager object and pass the menu that you need to start first as the start_menu parameter. Then .run() AsyncMenuManager object.

```python
menu_manager = AsyncMenuManager(start_menu=main_menu)
menu_manager.run()
```


## FAQ

### Terminal is flickering. How to fix it?
Try specifying screen_redraw_rate_in_seconds when instantiating the menu class. If this does not work, then try running the script in a different terminal emulator.
