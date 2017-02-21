# -*- coding: utf-8 -*-

import sys
import os

import pinboard
import click


def updateBookmarks(outfile, apiToken, includeTags):
	posts = getAllPosts(apiToken)
	writeBookmarks(posts, outfile, includeTags)


def getAllPosts(apiToken):
    pb = pinboard.Pinboard(apiToken)

    try:
        posts = pb.posts.all()
    except:
        click.echo("Error getting bookmarks from Pinboard")
        sys.exit(-1)
    else:
        #return json.load(posts)
        return posts


def writeBookmarks(posts, outfile, includeTags):
    output = ""

    for post in posts:
        description = post.description.encode('utf-8').replace(" ", "_")
        url = post.url.encode('utf-8')
        tags = post.tags

        if includeTags:
            line = "{} {} ;; {}".format(description, url, " ".join(tags).encode('utf-8'))
        else:
            line = "{} {}".format(description, url)

        output += "{}\n".format(line)

    outfile = os.path.abspath(os.path.expanduser(outfile))
    directory = os.path.dirname(outfile)
    if not os.path.exists(directory):
        os.makedirs(directory)


    with open(outfile, 'wb') as file:
        file.write(output)


def parsePost(post):
    pass


def validPost(post):
    return (post.description is not None and post.url is not None)
