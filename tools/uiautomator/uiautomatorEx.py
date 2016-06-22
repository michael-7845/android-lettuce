#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from myDevice import device as d

# 命令执行
def adb_shell(command):
    _command = r'shell ' + command
    p = d.server.adb.cmd(_command) #r"mkdir /sdcard/just4show" r"shell ls -la"
    (stdoutput,erroutput) = p.communicate() 
    return (stdoutput,erroutput)
    
# 文件系统
def listfile_under(dir, extension=None):
    _command = ""
    if extension == None:
        listpath = os.path.join(dir, "*")
        _command = "ls %s" % (listpath)
    else:
        listpath = os.path.join(dir, "*")
        _command = "ls %s.%s" % (listpath, extension)
        
    out = adb_shell(_command)[0].split("\n")
    files = []
    for fn in out:
        if fn.find(r"No such file or directory") >= 0:
            continue
        fname = re.sub("\s", "", fn)
        if len(fname) > 0:
            files.append(fname)
    return files
    
def delete_file(file):
    _command = "rm %s" % (file)
    adb_shell(_command)

def delete_allfiles_under(dir):
    path = os.path.join(dir, "*")
    _command = "rm %s" % (path)
    adb_shell(_command)
    
def delete_dir(dir):
    _command = "rm -rf %s" % (dir)
    adb_shell(_command)
    
def rename(old, new):
    _command = "mv %s %s" % (old, new)
    adb_shell(_command)
    
# Intent
def start_activity(act):
    _command = "am start -n %s" % (act)
    adb_shell(_command)
    d.wait.update()
    
if __name__ == '__main__':
    #print adb_shell("id")[0]
    print listfile_under(r"/sdcard/ykm")
    #print len(listfile_under(r"/sdcard/just4show/", "py"))
    #delete_file(r"/sdcard/just4show/3")
    #delete_allfiles_under(r"/sdcard/just4show")
    #delete_dir(r"/sdcard/just4show2")
    #rename(r"/sdcard/just4show", r"/sdcard/just4show2")
    #start_activity(r"com.android.calculator2/.Calculator")
    
    