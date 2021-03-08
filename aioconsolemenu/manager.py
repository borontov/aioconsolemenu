"""Menu managers classes."""
import asyncio
from typing import Optional

from aioconsolemenu.actions import SwitchMenuAction
from aioconsolemenu.menu import Menu


class AsyncMenuManager:
    """Asyncio menu manager."""

    def __init__(
        self,
        start_menu: Menu,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        """Init menu asyncio gather manager."""
        self.current_menu = start_menu
        self.loop = loop or asyncio.get_event_loop()

    def run(self) -> None:
        """Run asyncio gathers loop."""
        self.loop.run_until_complete(self.current_menu.start())
        while True:
            next_action = self.current_menu.asyncio_gather.result()
            if isinstance(next_action, SwitchMenuAction):
                self.current_menu = next_action.next_menu
            self.loop.run_until_complete(next_action.perform(self.loop))  # type: ignore
