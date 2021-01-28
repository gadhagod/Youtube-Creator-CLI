#!/usr/bin/env python
import click

import youtube
from .description import description

@click.group()
def channel():
    'Channel commands'

@channel.command(help='Get your channel stats')
def stats():
    me = youtube.get_me()
    print()
    print('Subscribers: ' + youtube.colors.green + youtube.commify(me['statistics']['subscriberCount']) + youtube.colors.end)
    print('Views: ' +  youtube.colors.green + youtube.commify(me['statistics']['viewCount']) + youtube.colors.end)
    print('Videos: ' + youtube.colors.green + youtube.commify(me['statistics']['videoCount']) + youtube.colors.end)
    print()

channel.add_command(description)