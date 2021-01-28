#!/usr/bin/env python
import click

import youtube

@click.group()
def description():
    'Description comands'

@description.command(help='View a video\'s description')
@click.argument('video-id')
def show(video_id):
    service = youtube.service()
    res = service.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()['items'][0]['snippet']['description']
    print(res)

@description.command(help='Update a video\'s description')
@click.argument('video-id')
@click.argument('updated-description')
def update(video_id, updated_description):
    service = youtube.service()
    res = service.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()['items'][0]['snippet']
    res['description'] = updated_description
    service.videos().update(
        part='snippet',
        body={
            'id': video_id,
            'snippet': res
        }
    ).execute()