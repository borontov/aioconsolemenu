"""Actions after done asyncio gather."""
import asyncio
import sys
from abc import abstractmethod

from aioconsolemenu import templates
from aioconsolemenu.menu import Menu
from aioconsolemenu.terminal_utils import clear_terminal


class Action:
    """Abstract action to do something after menu gather done."""

    async def perform(self, loop: asyncio.AbstractEventLoop) -> None:
        """Perform an action."""
        self.loop = loop
        await self.callback()

    @abstractmethod
    async def callback(self) -> None:
        """Action callback."""


class ExitAction(Action):
    """Exit from script action."""

    async def callback(self) -> None:
        """Exit callback."""
        clear_terminal()
        sys.exit(templates.EXIT.render())


class SwitchMenuAction(Action):
    """Switch menu action."""

    def __init__(
        self,
        current_menu: Menu,
        next_menu: Menu,
    ) -> None:
        """Init switch menu action."""
        self.current_menu = current_menu
        self.next_menu = next_menu

    async def callback(self) -> None:
        """Switch menu callback."""
        await self.next_menu.start()
