#!/usr/bin/env python
import click

import youtube

@click.group()
def description():
    'Description commands'

@click.group()
def description():
    'Description commands'

@description.command(help='Show your channel\'s description')
def show():
    'Show your channel\'s description'
    service = youtube.service()
    res = service.channels().list(
        part='snippet,contentDetails,statistics',
        mine=True
    ).execute()['items'][0]['snippet']
    print(res['description'])
    return res

@description.command(help='Update your channel\'s description')
@click.argument('updated-description')
def update(updated_description):
    'Update your channel\'s description'
    service = youtube.service()
    my_id = service.channels().list(
        part='snippet,contentDetails,statistics',
        mine=True
    ).execute()['items'][0]['id']
    
    service.channels().update(
        part='brandingSettings',
        body={
            'id': my_id,
            'brandingSettings': {
                'channel': {
                    'description': updated_description
                }
            }
        }
    ).execute()