#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import sys
import optparse
from uiautomator.myConfig import config

base_path = config.project.basepath

tips = '''
Usage: myimages.py [options] project
       myimages.py -h|--help for more help
'''

def _move(orig, dest):
    os.system(r"mv %s %s" % (orig, dest))
    
def _copy(orig, dest):
    os.system(r"cp -r %s %s" % (orig, dest))
    
def _move_update(orig, dest):
    os.system(r"mv -u %s %s" % (orig, dest))
    
def _copy_update(orig, dest):
    os.system(r"cp -r -u %s %s" % (orig, dest))
    
def _remove(path):
    os.system(r"rm -rf %s" % (path))
    
def __move(orig, dest):
    print r"mv %s %s" % (orig, dest)
#    
#def __copy(orig, dest):
#    print r"cp -r %s %s" % (orig, dest)
#    
#def __move_update(orig, dest):
#    print r"mv -u %s %s" % (orig, dest)
#    
#def __copy_update(orig, dest):
#    print r"cp -r -u %s %s" % (orig, dest)
#    
def __remove(path):
    print r"rm -rf %s" % (path)
    
def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options] project", version="%prog 1.0")
    
    parser.add_option("-d", 
                      dest="default",
                      action="store_true",
                      default=False,
                      help='specify project as default current project, which is specified in android_lettuce.conf/project/current, if project not specified')
    parser.add_option("-u", "--update", 
                      dest="update",
                      action="store_true",
                      default=False,
                      help='move/copy only when the SOURCE file is newer than the destination file or when the destination file is missing')
    parser.add_option("--cc", 
                      dest="cc",
                      action="store_true",
                      default=False,
                      help='clean the pictures under captures')
    parser.add_option("--ci", 
                      dest="ci",
                      action="store_true",
                      default=False,
                      help='clean the pictures under images')
    
    (options, args) = parser.parse_args(args)
    if len(args) == 1:
        captures_path = os.path.join(base_path, args[0], "captures", "*")
        images_path = os.path.join(base_path, args[0], "images")
    elif options.default:
        captures_path = os.path.join(base_path, config.project.current, "captures", "*")
        images_path = os.path.join(base_path, config.project.current, "images")
    else:
        print tips
        exit(1)
    
    if options.cc:
        _remove(captures_path)
        exit(0)
    
    if options.ci:
        _remove(os.path.join(images_path, "*"))
        exit(0)
    
    if options.update: # 只更新最新
        _copy_update(captures_path, images_path)
        exit(0)
    else: # 不考虑是否最新
        _copy(captures_path, images_path)
        exit(0)
        
        
    #parser.add_option("-k", "--keep", 
    #                  dest="keep",
    #                  action="store_true",
    #                  default=False,
    #                  help='whether the original files are kept')
    #parser.add_option("-c", "--clean", 
    #                  dest="clean",
    #                  action="store",
    #                  default=None,
    #                  help='clean the pictures under captures/images')
    
    #if options.clean:
    #    if (options.clean == "capture") or (options.clean == "captures"):
    #        _remove(captures_path)
    #    elif (options.clean == "image") or (options.clean == "images"):
    #        _remove(os.path.join(images_path, "*"))
    #    exit(0)
    
    #if options.update:
    #    if options.keep: # 保留原件, 只更新最新
    #        _copy_update(captures_path, images_path)
    #    else: # 不保留原件, 只更新最新
    #        _move_update(captures_path, images_path)
    #        _remove(captures_path)
    #    exit(0)
    #else:
    #    if options.keep: # 保留原件, 不考虑是否最新
    #        _copy(captures_path, images_path)
    #    else: # 不保留原件, 不考虑是否最新
    #        _move(captures_path, images_path)
    #        #_remove(captures_path)
    #    exit(0)
            
    
if __name__ == '__main__':
    commandui()
    