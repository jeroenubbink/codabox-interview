#!/usr/bin/env python

import sys
import urllib2

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: {} <id>".format(sys.argv[0])
        sys.exit(2)

    id = sys.argv[1]
    response = urllib2.urlopen('http://localhost/hello-world/{}'.format(id))

    print response.read()
