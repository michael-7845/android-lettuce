# -*- coding: utf-8 -*- 
import os
import sys
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *
import compimg
from uiautomator.myConfig import config

captures_dir = None
images_dir = None

def _update_captures_dir():
    project_dir = "."
    #print project_dir
    global captures_dir
    if not captures_dir:
        captures_dir = os.path.join(project_dir, "captures")
    if not os.path.exists(captures_dir):
        os.mkdir(captures_dir)
    #print "captures dir:", captures_dir
    
def _update_images_dir():
    steps_dir = os.path.dirname(_update_dirs.func_code.co_filename)
    project_dir = os.path.dirname(steps_dir)
    #print project_dir
    global images_dir
    if not images_dir:
        images_dir = os.path.join(project_dir, "images")
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
    #print "images dir:", images_dir

def _update_dirs():
    #steps_dir = os.path.dirname(_update_image_dir.func_code.co_filename)
    #project_dir = os.path.dirname(steps_dir)
    ##print project_dir
    #global captures_dir
    #global images_dir
    #if not captures_dir:
    #    captures_dir = os.path.join(project_dir, "captures")
    #if not images_dir:
    #    images_dir = os.path.join(project_dir, "images")
    #if not os.path.exists(captures_dir):
    #    os.mkdir(captures_dir)
    #if not os.path.exists(images_dir):
    #    os.mkdir(images_dir)
    _update_captures_dir()
    _update_images_dir()
    
_update_dirs()

def _capture(step, imgname):
    global captures_dir
    feature = step.scenario.feature
    scenario = step.scenario
    feature_dir = os.path.join(captures_dir, feature.name)
    scenario_dir = os.path.join(feature_dir, scenario.name)
    if not os.path.exists(feature_dir):
        os.mkdir(feature_dir)
    if not os.path.exists(scenario_dir):
        os.mkdir(scenario_dir)
    imgpath = os.path.join(scenario_dir, imgname+r".png")
    if os.path.exists(imgpath):
        os.remove(imgpath)
    d.screenshot(imgpath)
    
def _read_rect_file(rectfile):
    def _get_rect_from_line(line):
        r = line.strip().split(",")
        return tuple([int(s) for s in r])
    
    f = open(rectfile, 'r')
    rects = []
    for line in f:
        rects.append(_get_rect_from_line(line))
    f.close()
    return rects
    
def _get_rect(step, imgname):
    global images_dir
    feature = step.scenario.feature
    scenario = step.scenario
    rect_txt = os.path.join(images_dir, feature.name, scenario.name, imgname+r".txt")
    
    if not os.path.exists(rect_txt):
        return None
    return _read_rect_file(rect_txt)
    
def _compare(step, imgname):
    global captures_dir
    global images_dir
    feature = step.scenario.feature
    scenario = step.scenario
    captures_img = os.path.join(captures_dir, feature.name, scenario.name, imgname+r".png")
    images_img = os.path.join(images_dir, feature.name, scenario.name, imgname+r".png")
    print "_compare captures:", captures_img.encode("utf-8")
    print "_compare images:", images_img.encode("utf-8")
    
    if not os.path.exists(captures_img):
        return False
    if not os.path.exists(images_img):
        return False
    r = _get_rect(step, imgname)
    return compimg.isRectsMatch(subPath=captures_img.encode("utf-8"), srcPath=images_img.encode("utf-8"), threshold=0.005, rects=r, isAll=True)
    
@step(u'截屏【%s】$' % (mode_word))
def capture(step, imgname):
    _capture(step, imgname)
    
@step(u'截屏并比较【%s】$' % (mode_word))
def capture_compare(step, imgname):
    _capture(step, imgname)
    if config.image.is_compared:
        assert _compare(step, imgname)
    
# can not work until Android 4.2.
# 默认路径：home.png 即为与所执行feature同一级目录
# 自定义路径：/home/mike/home.png 
# 相对路径: captures/home.png
#@step(u'截取屏幕图片保存为【%s】$' % (mode_file))
def screenshot(step, path):
    d.screenshot(path)
    d.wait.idle()  
    