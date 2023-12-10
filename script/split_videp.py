'''
Split video by size or number of chunks

Original code: https://stackoverflow.com/a/28884437/1862500

@author yohanes.gultom@gmail.com
'''

import re
import math
from optparse import OptionParser

length_regexp = 'Duration: (\d{2}):(\d{2}):(\d{2})\.\d+,'
re_length = re.compile(length_regexp)

from subprocess import check_call, PIPE, Popen
import shlex

def main():
    opt = parse_options()
    filename = opt.filename
    split_size = opt.split_size
    split_count = opt.split_count

    if split_size and split_size <= 0:
        print("split_size can't be 0")
        raise SystemExit

    if split_count and split_count <= 1:
        print("split_count must be > 1")
        raise SystemExit

    p1 = Popen(["ffmpeg", "-i", filename], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # get p1.stderr as input
    output = Popen(["grep", 'Duration'], stdin=p1.stderr, stdout=PIPE, universal_newlines=True)
    p1.stdout.close()
    matches = re_length.search(output.stdout.read())
    if matches:
        video_length = int(matches.group(1)) * 3600 + \
                       int(matches.group(2)) * 60 + \
                       int(matches.group(3))
        print("Video length in seconds: {}".format(video_length))
    else:
        print("Can't determine video length.")
        raise SystemExit

    if split_count:
        print("split_count is defined. Ignoring split_size, if defined")
        split_size = math.ceil(video_length / split_count)

    if not split_count:
        split_count = math.ceil(video_length / split_size)
        if split_count == 1:
            print("Video length is less than the target split length.")
            raise SystemExit

    for n in range(split_count):
        split_start = split_size * n
        pth, ext = filename.rsplit(".", 1)
        cmd = "ffmpeg -i {} -vcodec copy  -strict -2 -ss {} -t {} {}-{}.{}".\
            format(filename, split_start, split_size, pth, n, ext)
        print("About to run: {}".format(cmd))
        check_call(shlex.split(cmd), universal_newlines=True)


def parse_options():
    parser = OptionParser()

    parser.add_option("-f", "--file",
                      dest="filename",
                      help="file to split, for example sample.avi",
                      type="string",
                      action="store"
    )
    parser.add_option("-s", "--split-size",
                      dest="split_size",
                      help="split or chunk size in seconds, for example 10",
                      type="int",
                      action="store"
    )
    parser.add_option("-c", "--split-count",
                      dest="split_count",
                      help="number of even-sized chunks, for example 4",
                      type="int",
                      action="store"
    )    
    (options, args) = parser.parse_args()

    if options.filename and (options.split_size or options.split_count):
        return options
    else:
        parser.print_help()
        raise SystemExit

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)