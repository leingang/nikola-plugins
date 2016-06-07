This plugin adds a menu of categories, with post counts, to the global context.

Usage
-----

Copy `category_menu.plugin` and `category_menu.py` to your Nikola site's
`plugins` directory.

This has only been tested with hierarchical categories.  The top level
categories are inserted into the menu, and the count is the count of all posts
with that category at the “top level.”

After installation, `site.GLOBAL_CONTEXT['CATEGORY_MENU']` will have a list of
tuples of the form `(link,count,name)`.  The list is sorted by reverse order of
post count.

It's up to you to do something with this, perhaps in a theme's template.
Included in this distribution are two templates for the mako version of
`bootstrap3`:

* a slightly modified `base.tmpl` to add the category menu to the navbar
* a template `category_menu.tmpl` to render that menu

Todo
----

* Double check that this works for non-hierarchical categories.
* Add support for multiple languages.  I think category names are not
internationalizable but the menu title “Categories” probably is.
* Allow other sorting methods, including manual sorting.
