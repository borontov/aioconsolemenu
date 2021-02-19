"""Menu class."""
import asyncio
from abc import abstractmethod
from contextlib import suppress
from typing import Optional

from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

from aioconsolemenu import templates
from aioconsolemenu.items import Items
from aioconsolemenu.paginator import Paginator
from aioconsolemenu.terminal_utils import clear_terminal


class Menu:
    """Class for create asyncio console menu instances."""

    def __init__(
        self,
        items: Items,
        items_per_page: Optional[int] = None,
        screen_redraw_rate_in_seconds: float = 0.4,
        title: Optional[str] = None,
    ) -> None:
        """Create menu instance."""
        self.items: Items = items
        self.items.sort_by_title_and_sort_id()
        self.paginator: Optional[Paginator]
        if items_per_page:
            self.paginator = Paginator(items, items_per_page)
        else:
            self.paginator = None
        self.screen_redraw_rate_in_seconds: float = screen_redraw_rate_in_seconds
        self.title = title

    @abstractmethod
    async def input_handler(self, input_text: str) -> None:
        """An abstract method forces you to refine the content of the input handler."""

    async def prompt_loop(self) -> None:
        """Async loop for menu prompt."""
        while True:
            try:
                self.loops.result()
            except asyncio.exceptions.InvalidStateError:
                input_text = await self.session.prompt_async("> ")
                await self.input_handler(input_text)
            else:
                return

    async def menu_loop(self) -> None:
        """Async loop for menu rendering."""
        while True:
            try:
                self.loops.result()
            except asyncio.exceptions.InvalidStateError:
                self.render()
                await asyncio.sleep(self.screen_redraw_rate_in_seconds)
            else:
                return

    async def start(self) -> None:
        """Start menu async loops."""
        self.session: PromptSession = PromptSession()
        self.loops = asyncio.gather(
            self.prompt_loop(),
            self.menu_loop(),
        )
        with suppress(asyncio.exceptions.CancelledError):
            with patch_stdout():
                await self.loops

    def format_page(self, page_items: list) -> Optional[str]:
        """Format items page as string."""
        title = templates.MENU_TITLE_TEMPLATE.render(title=self.title)
        items = templates.MENU_ITEMS_TEMPLATE.render(items=page_items)
        return "".join((title, items))

    def render(self) -> None:
        """Render items."""
        clear_terminal()
        if self.paginator:
            self.paginator.get_current_page_items()
            string = self.format_page(self.paginator.current_page_items)
        else:
            string = self.format_page(self.items)
        print(string)  # noqa: WPS421
