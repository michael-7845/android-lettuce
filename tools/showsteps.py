#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import re
import sys
import optparse
from glob import glob
from uiautomator.myConfig import config

project_root_path = config.project.basepath
tips = '''
Usage: showsteps.py [options] project
       showsteps.py -h|--help for more help
'''

def print_step(line):
    regex = r"^@step.*$"
    m = re.match(regex, line)
    if m is not None:
        print m.group()
    
def extract_from_file(filename):
    f = open(filename, 'r')
    for line in f:
        print_step(line)

def print_step2(line):
    regex = ur"@step.*'(\S+)\$'.*$"
    m = re.match(regex, line)
    if m is not None:
        print m.group(1)
        
def extract_from_file2(filename):
    f = open(filename, 'r')
    for line in f:
        print_step2(line)

def _locate(path, match):
    """Locate files recursively in a given path"""
    root_path = os.path.abspath(path)
    return_files = []
    return glob(os.path.join(root_path, match))

def _filename(path, with_extension=True):
    fname = os.path.split(path)[1]
    if not with_extension:
        fname = os.path.splitext(fname)[0]
    return fname

def show_step_under_dir(path, match, with_extension=True, extract_method=extract_from_file):
    files = _locate(path, match)
    filenames = []
    for (index, f) in enumerate(files):
        print 
        print index, _filename(f, with_extension)
        extract_method(f)

def main(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] project", version="%prog 1.0")

    parser.add_option("-s", 
                      dest="steppath",
                      action="store",
                      default=None,
                      help='show pre-defined steps under directory path, if project not specified')
    parser.add_option("-d", 
                      dest="default",
                      action="store_true",
                      default=False,
                      help='specify project as default current project, which is specified in android_lettuce.conf/project/current, if -s not specified')

    (options, args) = parser.parse_args(args)
    
    global path
    if len(args) == 1:
        path = os.path.join(project_root_path, args[0], "steps")
    elif options.steppath:
        path = options.steppath
    elif options.default:
        path = os.path.join(project_root_path, config.project.current, "steps")
    else:
        print tips
        exit(1)
    show_step_under_dir(path, '*.py', True)
    #show_step_under_dir('.', '*.py', False)

if __name__ == '__main__':
    main()
    
