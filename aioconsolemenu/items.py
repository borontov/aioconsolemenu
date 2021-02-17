"""Items."""
from typing import Any, Coroutine, Optional, Sequence

from infinity import Infinity


class InfinityInt(Infinity, int):  # noqa: WPS600
    """Infinity integer class."""


class Items(list):  # noqa: WPS600
    """Items class."""

    def __init__(self, seq: Sequence = ()) -> None:
        """Create items instance."""
        super().__init__()
        for title in seq:
            self.add(title=str(title))

    def add(
        self,
        title: str,
        item_data: Optional[dict] = None,
        sort_id: Optional[int] = InfinityInt(),
        callback: Optional[Coroutine] = None,
        args: Optional[tuple] = None,
    ) -> None:
        """Add item."""
        self.append(
            {
                "sort_id": sort_id,
                "title": title,
                "item_data": item_data,
                "callback": callback,
                "args": args,
            },
        )

    def sort_by_title_and_sort_id(self) -> None:
        """Sort items by title and sort id."""
        self.sort(key=lambda item: item["title"])
        self.sort(key=lambda item: item["sort_id"])

    def get_pagination_item(self, paginator: Any, action: str) -> dict:  # type: ignore
        """Get item for switch the page."""
        if action == "next_page":
            return {
                "sort_id": InfinityInt(),
                "title": "Next page",
                "item_data": None,
                "callback": paginator.next_page,
                "args": None,
            }
        elif action == "prev_page":
            return {
                "sort_id": InfinityInt(),
                "title": "Previous page",
                "item_data": None,
                "callback": paginator.prev_page,
                "args": None,
            }
