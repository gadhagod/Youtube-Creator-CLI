#!/usr/bin/env python
import click
import pickle
import os.path
from os import getenv
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

class colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

def service(version='v1'):
    try:
        creds = pickle.load(open(getenv('HOME') + '/.youtube-creators-cli/token.pickle', 'rb'))
    except FileNotFoundError:
        print('{}Not authorized. Run "yt login --help".{}'.format(colors.red, colors.end))
        exit()

    return build('youtube', version, credentials=creds)
    
def get_me():
    return(service().channels().list(
        part="snippet,contentDetails,statistics",
        mine=True
    ).execute()['items'][0])

def commify(in_int):
    return '{:,}'.format(int(in_int))