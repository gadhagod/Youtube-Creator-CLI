#!/usr/bin/env python
import click

import youtube

@click.group()
def title():
    'Title commands'

@title.command(help='View a video\'s title')
@click.argument('video-id')
def show(video_id):
    service = youtube.service()
    res = service.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()['items'][0]['snippet']['title']
    print(res)

@title.command(help='Update a video\'s title')
@click.argument('video-id')
@click.argument('updated-description')
def update(video_id, updated_description):
    service = youtube.service()

    snippet = service.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()['items'][0]['snippet']

    snippet['title'] = updated_description

    res = service.videos().update(
        part='snippet',
        body={
            'id': video_id,
            'snippet': snippet
        }
    ).execute()

    print(res)