"""Items."""
from typing import Callable, Optional

from infinity import Infinity

from aioconsolemenu import templates


class InfinityInt(Infinity, int):  # noqa: WPS600
    """Infinity integer class."""


class Items(list):  # noqa: WPS600
    """Items class."""

    def sort(self) -> None:  # type: ignore
        """Sort items first by title and then by sort id."""
        sorting_order = [lambda item: item.title, lambda item: item.sort_id]
        for key in sorting_order:
            super().sort(key=key)


class Item:
    """Menu item class."""

    def __init__(
        self,
        title: str,
        item_data: Optional[dict] = None,
        sort_id: Optional[int] = InfinityInt(),
        callback: Callable = None,
        kwargs: Optional[dict] = None,
    ) -> None:
        """Item init."""
        self.title = title
        self.item_data = item_data
        self.sort_id = sort_id
        self.callback = callback
        self.kwargs = kwargs or dict()


class NextPageItem(Item):
    """Next page item."""

    def __init__(
        self,
        callback: Callable,  # type: ignore
        title: str = templates.NEXT_PAGE_ITEM_TITLE.render(),
    ) -> None:
        """Init."""
        super().__init__(callback=callback, title=title)


class PrevPageItem(Item):
    """Previous page item."""

    def __init__(
        self,
        callback: Callable,  # type: ignore
        title: str = templates.PREV_PAGE_ITEM_TITLE.render(),
    ) -> None:
        """Init."""
        super().__init__(callback=callback, title=title)
