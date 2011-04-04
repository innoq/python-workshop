#!/usr/bin/env python

"""
Usage:
  $ logparse.py <filepath> <filter term> [level]
"""

import sys


def main(args):
    args = [unicode(arg, 'utf-8') for arg in args]

    try:
        filepath = args[1]
        filterm = args[2] # XXX: rename
    except IndexError:
        print "missing argument"
        print __doc__
        return False
    try:
        level = args[3]
    except IndexError:
        level = "INFO"

    fh = open(filepath) # NB: might use `with` in later versions

    messages = {
        "DEBUG": [],
        "INFO": [],
        "ERROR": []
    }
    for line in fh:
        date, time, level, msg = line.split(" ", 3)
        timestamp = "%s %s" % (date, time)
        message = {
            "timestamp": timestamp,
            "text": msg.strip()
        }
        messages[level].append(message)

    fh.close()

    for msg in messages[level]:
        if filterm in msg["text"]:
           print msg

    return True


if __name__ == '__main__':
    status = not main(sys.argv)
    sys.exit(status)
