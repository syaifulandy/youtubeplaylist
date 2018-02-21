#!/usr/bin/env python
import os, sys, time
import argparse
from urllib2 import urlopen

import pytube  # pip install pytube

from pytube import YouTube

#Link playlist
Link_playlist_url ="https://www.youtube.com/playlist?list=PLxhvVyxYRviZd1oEA9nmnilY3PhVrt4nj"

def get_playlist_links(playlist_url):
    page_elements = urlopen(playlist_url).readlines()
    video_elements = [el for el in page_elements if 'pl-video-title-link' in el]  # Filter out unnecessary lines
    video_urls = [v.split('href="',1)[1].split('" ',1)[0] for v in video_elements]  # Grab the video urls from the elements
    return ['http://www.youtube.com' + v for v in video_urls]


start_time = time.time()

def print_dot(bytes_received, file_size, start):
    global start_time
    if time.time() - start_time > 1.0:
        sys.stdout.write('.')
        sys.stdout.flush()
        start_time = time.time()


parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-p PLAYLISTURL] [-d DESTINATION]')
parser.add_argument('-p', '--playlisturl', help='url of the playlist to be downloaded', default=Link_playlist_url, metavar='')
parser.add_argument('-d', '--destination', help='path of directory to save videos to', default=os.path.curdir, metavar='')
args = parser.parse_args()


if os.path.exists(args.destination):
    directory_contents = [f.split('.mp4',1)[0] for f in os.listdir(args.destination) if f.endswith('.mp4')]
else:
    print('Destination directory does not exist')
    sys.exit(1)

video_urls = get_playlist_links(args.playlisturl)
confirmation = raw_input('You are about to download {} videos to {}\nWould you like to continue? [Y/n] '.format(
    len(video_urls), os.path.abspath(args.destination)))

i = 1
#Tuliskan playlist yang gak mau di donlod
jangandonlod = []
if confirmation.lower() in ['y', '']:
    for u in video_urls:
        yt = YouTube(u)
        print yt.title
        caption = yt.captions.get_by_language_code('en')
        file = open(yt.title+".srt","w")
        file.write(caption.generate_srt_captions())
        file.close()
        print i
        stream = yt.streams.all()
        stream = stream[2]
        print stream
        if (i in jangandonlod):
            print "gak donlod"
        else:
            stream.download()
        i = i + 1
        #stream.download()
print('Done')
