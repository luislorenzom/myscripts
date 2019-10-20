import random
import shutil
import os

MUSIC_FILES = list()
MUSIC_CANDIDATES = set()

PLAYLIST_SIZE = 300
MUSIC_DEVICE_FOLDER = '/run/user/1000/gvfs/mtp:host=%5Busb%3A001%2C043%5D/Almacenamiento interno compartido/Music'
MUSIC_FOLDERS = [
    '/media/luis/Luis/Musica/discos',
    '/media/luis/Luis/Musica/musica_suelta'
]

def get_files_from_folder(folder_path):
    with os.scandir(folder_path) as folder:
        for file in folder:
            if file.is_file() and (file.name.endswith('.mp3') or file.name.endswith('.flac')):
                MUSIC_FILES.append(file)
            elif file.is_dir():
                get_files_from_folder(file.path)

def copy(src, dst):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    shutil.copyfile(src, dst)

# Get all files
for folder_path in MUSIC_FOLDERS:
    get_files_from_folder(folder_path)

# We shuffle the list to increase the random selection
random.shuffle(MUSIC_CANDIDATES)

# Get the file candidates
for i in range(PLAYLIST_SIZE):
    index = random.randrange(0, len(MUSIC_FILES))
    MUSIC_CANDIDATES.add(MUSIC_FILES[index])

# Remove device music files
with os.scandir(MUSIC_DEVICE_FOLDER) as device_folder:
    for file in device_folder:
        os.remove(file.path)

# Copy new ones
for file in MUSIC_CANDIDATES:
    copy(file.path, MUSIC_DEVICE_FOLDER)