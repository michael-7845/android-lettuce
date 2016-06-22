#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import sys
from lettuce import *

from lettuce.regex import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
    
@step(u'执行shell命令【%s】$' % (mode_text))
def run_command(step, command):
    ex.adb_shell(command.strip())
    
@step(u'设置路径【%s】文件数检查点$' % (mode_file))
def set_filecounter_checkpoint(step, path):
    files = ex.listfile_under(path.strip())
    if not hasattr(world, "file_counter"):
        world.file_counter = {}
    world.file_counter[path] = len(files)
@step(u'路径【%s】文件数相对上个检查点应该增加【%s】$' % (mode_file, mode_int))
def check_filecounter_plus(step, path, incr):
    files = ex.listfile_under(path.strip())
    assert (len(files)==(world.file_counter[path]+int(incr))), "文件数变化不符合预期"
    del world.file_counter[path] #删除此计数器
@step(u'路径【%s】文件数相对上个检查点应该减少【%s】$' % (mode_file, mode_int))
def check_filecounter_sub(step, path, incr):
    files = ex.listfile_under(path.strip())
    assert (len(files)==(world.file_counter[path]-int(incr))), "文件数变化不符合预期"
    del world.file_counter[path] #删除此计数器
    
@step(u'设置路径【%s】下【%s】类型文件数检查点$' % (mode_file, mode_word))
def set_filecounter_checkpoint_by_extension(step, path, extension):
    files = ex.listfile_under(path.strip(), extension)
    if not hasattr(world, "file_counter"):
        world.file_counter = {}
    world.file_counter[path] = len(files)
@step(u'路径【%s】下【%s】类型文件数相对上个检查点应该增加【%s】$' % (mode_file, mode_word, mode_int))
def check_filecounter_plus_by_extension(step, path, extension, incr):
    files = ex.listfile_under(path.strip(), extension)
    assert (len(files)==(world.file_counter[path]+int(incr))), "文件数变化不符合预期"
    del world.file_counter[path] #删除此计数器
@step(u'路径【%s】下【%s】类型文件数相对上个检查点应该减少【%s】$' % (mode_file, mode_word, mode_int))
def check_filecounter_sub_by_extension(step, path, extension, incr):
    files = ex.listfile_under(path.strip(), extension)
    assert (len(files)==(world.file_counter[path]-int(incr))), "文件数变化不符合预期"
    del world.file_counter[path] #删除此计数器
    
@step(u'路径【%s】下应该存在文件【%s】$' % (mode_file, mode_file))
def is_file_exsited(step, path, file):
    files = ex.listfile_under(path.strip())
    print files
    print file
    print
    filenames = []
    for f in files:
        filenames.append(os.path.split(f)[1])
    assert (file in filenames), "目录下不存在文件"
    
@step(u'删除文件【%s】$' % (mode_file))
def del_file(step, file):
    ex.delete_file(file)
    
@step(u'删除路径【%s】下所有文件$' % (mode_file))
def del_files_under_dir(step, dir):
    ex.delete_allfiles_under(dir)
    
@step(u'删除目录【%s】$' % (mode_file))
def del_dir(step, dir):
    ex.delete_dir(dir)
    
@step(u'文件或目录【%s】改为【%s】$' % (mode_file, mode_file))
def move(step, old, new):
    ex.rename(old, new)
    
if __name__ == '__main__':
    #print ex.adb_shell("id")[0]
    #ex.adb_shell(r"mkdir /sdcard/ykm")
    #print listfile_under(r"/sdcard/just4show/", "py")
    #print len(listfile_under(r"/sdcard/just4show/", "py"))
    #delete_file(r"/sdcard/just4show/3")
    #delete_allfiles_under(r"/sdcard/just4show")
    #ex.delete_dir(r"/sdcard/ykm")
    #rename(r"/sdcard/just4show", r"/sdcard/just4show2")
    #start_activity(r"com.android.calculator2/.Calculator")
    if not hasattr(world, "file_counter"):
        world.file_counter = {}
    world.file_counter['abc'] = 3
