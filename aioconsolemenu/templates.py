"""Mako templates."""
import os

from mako.lookup import TemplateLookup

templates_dir = os.path.abspath("aioconsolemenu/templates/")

lookup = TemplateLookup(
    [
        templates_dir,
    ],
)

NEXT_PAGE_ITEM_TITLE = lookup.get_template("next_page_item_title.txt")
PREV_PAGE_ITEM_TITLE = lookup.get_template("prev_page_item_title.txt")
MENU_ITEMS_TEMPLATE = lookup.get_template("menu_items.txt")
MENU_TITLE_TEMPLATE = lookup.get_template("menu_title.txt")
SELECT_OUT_OF_AVAILABLE_OPTIONS = lookup.get_template(
    "select_out_of_available_options.txt",
)
PAGE_DOES_NOT_EXIST = lookup.get_template("page_does_not_exist.txt")
EXIT = lookup.get_template("exit.txt")
