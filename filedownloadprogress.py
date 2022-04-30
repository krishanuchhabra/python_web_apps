#!/usr/bin/env python

import urllib,sys

def progress(nblocks, block_size, file_size):
    print (nblocks*block_size*100)/float(file_size)



url=sys.argv[1]

local_file = "PYTHON_DOWNLOAD.tar.bz2"

urllib.urlretrieve(url, local_file, progress)
