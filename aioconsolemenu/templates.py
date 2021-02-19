"""Mako templates."""
import os

from mako.lookup import TemplateLookup

templates_dir = os.path.abspath("aioconsolemenu/templates/")

lookup = TemplateLookup(
    [
        templates_dir,
    ],
)


MENU_ITEMS_TEMPLATE = lookup.get_template("/menu_items.txt")
MENU_TITLE_TEMPLATE = lookup.get_template("/menu_title.txt")
SELECT_OUT_OF_AVAILABLE_OPTIONS = lookup.get_template(
    "/select_out_of_available_options.txt",
)
