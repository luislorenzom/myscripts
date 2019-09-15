# -*- coding: utf-8 -*-

# For youtube-dl updates ~> "pip install --upgrade youtube-dl"

from __future__ import unicode_literals
from os import listdir
from os.path import isfile
from environs import Env

import os
import json
import youtube_dl

# ----------------------
# Constants
# ----------------------
env = Env()
env.read_env('../.env')
DOWNLOAD_FOLDER = env('DOWNLOAD_FOLDER')
SOURCE_FILE = env('SOURCE_FILE') 
BOOKMARK_ROOT_FOLDER_NAME = env('BOOKMARK_ROOT_FOLDER_NAME')

# ----------------------
# Get urls
# ----------------------
f = open(SOURCE_FILE, 'r')
bookmarks = f.read()
f.close()

bookmarks_as_json = json.loads(bookmarks)
music_root_folder_index = 0
for i in list(bookmarks_as_json['roots']['bookmark_bar']['children']):
    if i['name'] == BOOKMARK_ROOT_FOLDER_NAME:
        break
    music_root_folder_index += 1

urls = [i['url'] for i in list(bookmarks_as_json['roots']['bookmark_bar']['children'])[music_root_folder_index]['children']]

# ----------------------
# Download and convert
# ----------------------
class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print(d['filename'][:-16] + ' ~> Done downloading, now converting...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

# ----------------------
# Rename files
# ----------------------
songs = [f for f in listdir('.') if isfile(f) and f[0]!='.' and f[-3:] == 'mp3']
DOWNLOAD_FOLDER = DOWNLOAD_FOLDER + '/' if DOWNLOAD_FOLDER[-1] != '/' else DOWNLOAD_FOLDER

for song in songs:
    newSongName = song[:-16] + '.mp3'
    os.renames(song, DOWNLOAD_FOLDER + newSongName)
