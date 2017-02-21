# -*- coding: utf-8 -*-

import sys
import click
import pinboard

from surfrawpinboard import bookmarks

@click.command()
@click.argument('outfile')
@click.option('--token', '-t', help="Pinboard API token.")
@click.option('--tags/--no-tags', default=True, help="Include tags in the output.")
@click.version_option()
def main(outfile, token, tags):
    """Script to export Pinboard bookmarks to a surfraw bookmark files"""
    if not token:
        click.secho('Please, specify a valid API token for Pinboard. See https://pinboard.in/settings/password for information.', fg="red")
        sys.exit(-1)

    bookmarks.updateBookmarks(outfile, token, tags)


if __name__ == "__main__":
    main()
