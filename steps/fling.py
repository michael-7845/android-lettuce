# -*- coding: utf-8 -*- 
# swipe 滑动
# drag 拖动
# fling 快速滑动
# scroll 滚动
import re,sys
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

# *-* 快速滑动 *-* 
# 简约写法
@step(u'手指快速向左滑动屏幕$')
def flingLeft(step):
    d().fling.horiz.forward()
    d.wait.idle()
    
@step(u'手指快速向右滑动屏幕$')
def flingRight(step):
    d().fling.horiz.backward()
    d.wait.idle()

@step(u'手指快速向上滑动屏幕$')
def flingUp(step):
    d().fling.vert.forward()
    d.wait.idle()

@step(u'手指快速向下滑动屏幕$')
def flingEnd(step):
    d().fling.vert.backward()
    d.wait.idle()
    
# 到起始/结束位置
#注意：可能布局问题，手指快速滑动的起始位置不在listView上
#可能会滑动失败，如Settings从上往下快速滑动，
#起始点在Title控件上而非列表中。
#建议：使用滑动框架的方法
@step(u'手指快速向上边起始位置滑动$')
def flingVertEnd(step):
    d().fling.vert.toEnd()
    d.wait.idle()

@step(u'手指快速向下边结束位置滑动$')
def flingVertBegin(step):
    d().fling.vert.toBeginning()
    d.wait.idle()
    
@step(u'手指快速向左边起始位置滑动$')
def flingHorizEnd(step):
    d().fling.horiz.toEnd()
    d.wait.idle()

@step(u'手指快速向右边结束位置滑动$')
def flingHorizBegin(step):
    d().fling.horiz.toBeginning()
    d.wait.idle()
    
# *-* 快速滑动框架 *-*
# 简约写法
@step(u'手指快速向左滑动框架【%s】$' % (mode_pvs))
def flingLeft(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.horiz.forward()
    d.wait.idle()
    
@step(u'手指快速向右滑动框架【%s】$' % (mode_pvs))
def flingRight(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.horiz.backward()
    d.wait.idle()

@step(u'手指快速向上滑动框架【%s】$' % (mode_pvs))
def flingUp(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.vert.forward()
    d.wait.idle()

@step(u'手指快速向下滑动框架【%s】$' % (mode_pvs))
def flingEnd(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.vert.backward()
    d.wait.idle()

# 到起始/结束位置
@step(u'手指快速向上边起始位置滑动框架【%s】$' % (mode_pvs))
def flingVertEnd(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.vert.toEnd()
    d.wait.idle()

@step(u'手指快速向下边结束位置滑动框架【%s】$' % (mode_pvs))
def flingVertBegin(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.vert.toBeginning()
    d.wait.idle()
    
@step(u'手指快速向左边起始位置滑动框架【%s】$' % (mode_pvs))
def flingHorizEnd(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.horiz.toEnd()
    d.wait.idle()

@step(u'手指快速向右边结束位置滑动框架【%s】$' % (mode_pvs))
def flingHorizBegin(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).fling.horiz.toBeginning()
    d.wait.idle()