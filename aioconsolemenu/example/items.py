"""Items for demo menus."""
from aioconsolemenu.example.handlers import (
    first_item_handler,
    other_items_handler,
    second_item_handler,
    submenu_exit_handler,
)
from aioconsolemenu.items import Item, Items

items1 = Items()
items1.append(Item("Second item (submenu)", callback=second_item_handler, sort_id=5))
items1.append(Item("4-h item (print)", callback=other_items_handler))
items1.append(Item("3-h item (print)", callback=other_items_handler))
items1.append(Item("First item (exit)", callback=first_item_handler, sort_id=3))

items2 = Items()
for title in range(200, 300):  # noqa: WPS432
    items2.append(Item(f"{title} (print)", callback=other_items_handler))
items2.append(Item("return to main menu", callback=submenu_exit_handler, sort_id=0))
