#!/usr/bin/env python

import eyed3
import os
import sys

from optparse import OptionParser

def update_id3(file_path, options):
    audio_file = eyed3.load(file_path)

    if options.id3_album:
        audio_file.tag.album = unicode(options.id3_album)
    if options.id3_artist:
        audio_file.tag.artist = unicode(options.id3_artist)
    if options.id3_title:
        audio_file.tag.title = unicode(options.id3_title)
    if options.sync_title:
        audio_file.tag.title = unicode(get_file_name(file_path))

    audio_file.tag.save()

def dump_id3(file_path):
    audio_file = eyed3.load(file_path)
    print audio_file.tag.album
    print audio_file.tag.artist
    print audio_file.tag.title

def get_file_name(file_path):
    file_name = os.path.basename(file_path)
    file_name = file_name.split('.')[0]
    return file_name

def get_file_list(directory):
    path_list = []
    file_list = os.listdir(directory)

    for f in file_list:
        if os.path.splitext(f)[1] == '.mp3':
            path_list.append(os.path.join(directory, f))

    return path_list

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file",
                      action="store",
                      type="string",
                      dest="file_name",
                      help="the file to be handled")
    parser.add_option("-d", "--directory",
                      action="store",
                      type="string",
                      dest="dir_name",
                      help="the directory contains all the file needed handled")
    parser.add_option("--artist",
                      action="store",
                      type="string",
                      dest="id3_artist",
                      help="the artist of the mp3 file")
    parser.add_option("--album",
                      action="store",
                      type="string",
                      dest="id3_album",
                      help="the album of the mp3 file")
    parser.add_option("--title",
                      action="store",
                      type="string",
                      dest="id3_title",
                      help="the title of the mp3 file")
    parser.add_option("--sync_title",
                      action="store_true",
                      dest="sync_title",
                      help="fill the title with file name, it will cover the '--title' options")
    (options, args) = parser.parse_args()

    file_list = []
    if options.dir_name:
        file_list = get_file_list(options.dir_name)
    elif options.file_name:
        file_list.append(options.file_name)

    if file_list:
        for f in file_list:
            update_id3(f, options)

        print 'Done. Enjoy it.'

if __name__ == "__main__":
    sys.exit(main())
