"""Custom menus."""
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
            print(templates.SELECT_OUT_OF_AVAILABLE_OPTIONS.render())  # noqa: WPS421
        else:
            await target_list[item_id]["callback"](self)
