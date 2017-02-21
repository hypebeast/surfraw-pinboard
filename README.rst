===============================
Surfraw-Pinboard
===============================

Simple Python command line tool to download bookmarks from https://pinboard.in and save it in the `surfraw <https://surfraw.alioth.debian.org>` _ bookmark format.

The bookmark file can then be used together with `Rofi <https://davedavenport.github.io/rofi/>` _ and `surfraw <https://surfraw.alioth.debian.org>` _
to implement a bookmark manager.

See `rofi-surfraw-bookmark.sh <https://github.com/hypebeast/dotfiles/blob/master/bin/bin/rofi-surfraw-bookmark.sh>` _ as an example
how to use Rofi as a bookmark manager.

.. image:: https://img.shields.io/pypi/v/surfraw_pinboard.svg
        :target: https://pypi.python.org/pypi/surfraw_pinboard


* Free software: MIT license


Features
--------

* Download all your bookmarks from `Pinboard <https://pinboard.in>` _.
* Bookmarks are saved in surfraw bookmark formt.

Usage
-----

Install it with:

``pip install surfraw-pinboard``

Then start downloading your bookmarks with:

``surfraw-pinboard -t 'token' bookmarks.txt``

Get your token at `Pinboard <https://pinboard.in/settings/password>` _.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
