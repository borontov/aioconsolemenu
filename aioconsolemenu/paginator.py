"""Paginator for menu."""
import math
from typing import Any, List

from aioconsolemenu import templates
from aioconsolemenu.items import Items, NextPageItem, PrevPageItem


class Paginator:
    """Class of paginator."""

    def __init__(self, items: Items, items_per_page: int) -> None:
        """Create paginator instance."""
        self.current_page: int = 1
        self.items = items
        self.current_page_items: List[dict] = []
        self.items_per_page: int = items_per_page
        self.pages_count = math.ceil(len(self.items) / self.items_per_page)

    async def next_page(self, *args: Any) -> None:
        """Switch page to next."""
        self.set_page(self.current_page + 1)

    async def prev_page(self, *args: Any) -> None:
        """Switch page to previous."""
        self.set_page(self.current_page - 1)

    def set_page(self, page: int) -> None:
        """Set current page."""
        if page in range(1, self.pages_count + 1):
            self.current_page = int(page)
        else:
            print(templates.PAGE_DOES_NOT_EXIST.render())  # noqa: WPS421

    def get_current_page_items(self) -> None:  # noqa: WPS615, WPS463
        """Set current page items to self.current_page_items."""
        if self.current_page == 1:
            start_index = 0
            end_index = self.items_per_page
        else:
            start_index = self.current_page * self.items_per_page - self.items_per_page
            end_index = self.current_page * self.items_per_page
        self.current_page_items = self.items[start_index:end_index]
        self.add_pagination_items()

    def add_pagination_items(self) -> None:
        """Add items for pagination."""
        if self.pages_count > 1:
            if self.current_page == 1:
                self.current_page_items.append(
                    NextPageItem(callback=self.next_page),  # type: ignore
                )
            elif self.current_page < self.pages_count:
                self.current_page_items.append(
                    PrevPageItem(callback=self.prev_page),  # type: ignore
                )
                self.current_page_items.append(
                    NextPageItem(callback=self.next_page),  # type: ignore
                )
            else:
                self.current_page_items.append(
                    PrevPageItem(callback=self.prev_page),  # type: ignore
                )
