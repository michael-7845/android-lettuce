#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import sys
import optparse
from glob import glob
from uiautomator.myDevice import device as d

base_path = r"/home/ckt/lettuce/viewer"
current_path = os.getcwd()

def goto_basepath(basepath):
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    os.chdir(basepath)
    
def _locate(path, match):
    return glob(os.path.join(path, match))

def _filename(path, with_extension=True):
    fname = os.path.split(path)[1]
    if not with_extension:
        fname = os.path.splitext(fname)[0]
    return fname

def rename(path):
    if os.path.exists(path):
        xml = os.path.join(path, r"*.xml")
        uix = os.path.join(path, r"*.uix")
        os.rename(xml, uix)

def rename(path, old_postfix, new_postfix):
    xmls = _locate(path, r"*."+old_postfix)
    for old in xmls:
        fn = _filename(old, with_extension=False)
        new = os.path.join(path, "%s.%s" % (fn, new_postfix))
        print old
        print new
        os.rename(old, new)

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")

    parser.add_option("-n", "--pagename", 
                      dest="pagename",
                      action="store",
                      default="mypage",
                      help='provide the page name')
    parser.add_option("-p", "--path", 
                      dest="path",
                      action="store",
                      default=base_path,
                      help='specify the store path')
     
    (options, args) = parser.parse_args(args)
    
    goto_basepath(options.path)
    capture(options.pagename)
    rename(options.path, "xml", "uix")
    os.chdir(current_path)

def capture(pagename):
    d.dump("%s.xml" % pagename)
    d.screenshot("%s.png" % pagename)

if __name__ == '__main__':
    commandui()
