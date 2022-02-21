from pytube import YouTube
import os, ssl
import sys


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def main(argv):
    if len(argv) == 1:
        yt = YouTube(argv[0])
        yt.streams.get_highest_resolution().download(
            os.path.expanduser('~/Desktop/videos'), )

        print('successfully downloaded video to Desktop')

    if len(argv) == 2:
        YouTube(argv[0]).streams.get_highest_resolution().download(
            argv[1])
        print(f'successfully downloaded video to {argv[1]}')

    if len(argv) > 2 or len(argv) <= 0:
        print('invalid number of arguments')
        return


main(sys.argv[1:])
