"""Items for demo menus."""
from aioconsolemenu.example.handlers import (
    first_item_handler,
    other_items_handler,
    second_item_handler,
)
from aioconsolemenu.items import Items

items1 = Items()
items1.add("Second item", callback=second_item_handler, sort_id=5)
items1.add("4-h item", callback=other_items_handler)
items1.add("3-h item", callback=other_items_handler)
items1.add("First item", callback=first_item_handler, sort_id=3)

items2 = Items()
for title in range(200, 300):  # noqa: WPS432
    items2.add(
        title=str(title),
        callback=other_items_handler,
    )
