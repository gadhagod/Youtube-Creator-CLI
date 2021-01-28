#!/usr/bin/env python
import click
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

import youtube
from .title import title
from .description import description

@click.group()
def video():
    'Video commands'

@video.command(help='View a video\'s stats')
@click.argument('video-id')
def stats(video_id):
    service = youtube.service()
    res = service.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()['items'][0]

    print()
    print('Views: ' + youtube.colors.green + youtube.commify(res['statistics']['viewCount']) + youtube.colors.end)
    print('Likes: ' + youtube.colors.green + youtube.commify(res['statistics']['likeCount']) + youtube.colors.end)
    print('Dislikes: ' + youtube.colors.green + youtube.commify(res['statistics']['dislikeCount']) + youtube.colors.end)
    print('Favorites: ' + youtube.colors.green + youtube.commify(res['statistics']['favoriteCount']) + youtube.colors.end)
    print()

@video.command(help='Upload a video')
@click.argument('filename', type=click.Path(exists=True))
@click.option('-t', '--title')
@click.option('-d', '--description', default='')
@click.option('--tags', default=False)
@click.option('-c', '--category', default=False, type=click.INT)
@click.option('-v', '--visibility', default='public')
def upload(filename, title, description, tags, category, visibility):
    if visibility not in ['public', 'private', 'unlisted']:
        print('Invalid visibility. Must be "public" (default), "private", or "unlisted".')
    body = {
        'snippet': {
            'title': title,
            'description': description,
        },
        'status': {
            'privacyStatus': visibility
        }
    }
    if tags:
        body['snippet']['tags'] = tags.split(', ')
    if category:
        body['snippet']['categoryId'] = str(category)

    service = youtube.service(version='v3')
    service.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(filename)
    ).execute()

@video.command(help='Delete a video')
@click.argument('video-id')
@click.option('-r', '--remove', help='Force remove.')
def delete(video_id, remove):
    service = youtube.service()
    try:
        vid_name = service.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()['items'][0]['snippet']['title']
    except:
        print('{}Video doesn\'t exist.{}'.format(youtube.colors.red, youtube.colors.end))
        exit()

    if not remove:
        if input('Are your sure you would like to delete "{}{}{}"? Y/N: '.format(youtube.colors.yellow, vid_name, youtube.colors.end)).lower() == 'y':
            remove = True

    if remove:
        try:
            service.videos().delete(
                id=video_id
            ).execute()
        except HttpError:
            print('{}You are trying to delete a video you don\'t own.{}'.format(youtube.colors.red, youtube.colors.end))
    else:
        print('Aborted!')

video.add_command(title)
video.add_command(description)