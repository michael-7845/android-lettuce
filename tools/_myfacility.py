#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
import optparse
from uiautomator.myConfig import config

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")
    
    parser.add_option("-b", 
                      dest="basepath",
                      action="store_true",
                      default=False,
                      help='get projct basepath, which is specified in android_lettuce.conf/project/basepath')
    
    (options, args) = parser.parse_args(args)
    
    if options.basepath:
        print config.project.basepath
        exit(0)

if __name__ == '__main__':
    commandui()
