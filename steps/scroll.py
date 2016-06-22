# -*- coding: utf-8 -*- 
# swipe 滑动
# drag 拖动
# fling 快速滑动
# scroll 滚动
import re,sys
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *


# *-* 滚动 *-*
# 简约写法
@step(u'手指向左滚动屏幕$')
def scrollToDown(step):
    d().scroll.horiz.forward()
    d.wait.idle()

@step(u'手指向右滚动屏幕$')
def scrollToDown(step):
    d().scroll.horiz.backward()
    d.wait.idle()

@step(u'手指向上滚动屏幕$')
def scrollToDown(step):
    d().scroll.vert.forward()
    d.wait.idle()
    
@step(u'手指向下滚动屏幕$')
def scrollToDown(step):
    d().scroll.vert.backward()
    d.wait.idle()
    
# 步长
@step(u'以步长【%s】手指向左滚动$' % (mode_int))
def scrollLeftByStep(step, cond):
    steps = {}
    steps['steps'] = cond
    d().scroll.horiz.forward(**steps)
    d.wait.idle()

@step(u'以步长【%s】手指向右滚动$' % (mode_int))
def scrollRightByStep(step, steps):
    steps = {}
    steps['steps'] = cond
    d().scroll.horiz.backward(**steps)
    d.wait.idle()

@step(u'以步长【%s】手指向上滚动$' % (mode_int))
def scrollUpByStep(step, steps):
    steps = {}
    steps['steps'] = cond
    d().scroll.vert.forward(**steps)
    d.wait.idle()
    
@step(u'以步长【%s】手指向下滚动$' % (mode_int))
def scrollDownByStep(step, steps):
    steps = {}
    steps['steps'] = cond
    d().scroll.vert.backward(**steps)
    d.wait.idle()
    
# 到起始/结束位置
@step(u'手指向左边起始位置滚动$')
def scrollHorizToEnd(step):
    d().scroll.horiz.toEnd()
    d.wait.idle()
    
@step(u'手指向右边结束位置滚动$')
def scrollHorizToBegin(step):
    d().scroll.horiz.toBeginning()
    d.wait.idle()

@step(u'手指向上边起始位置滚动$')
def scrollVertToEnd(step):
    d().scroll.vert.toEnd()
    d.wait.idle()

@step(u'手指向下边结束位置滚动$')
def scrollVertToBegin(step):
    d().scroll.vert.toBeginning()
    d.wait.idle()

# *-* 滚动框架 *-*
# 简约写法
@step(u'手指向左滚动框架【%s】$' % (mode_pvs))
def scrollToDown(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.forward()
    d.wait.idle()

@step(u'手指向右滚动框架【%s】$' % (mode_pvs))
def scrollToDown(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.backward()
    d.wait.idle()

@step(u'手指向上滚动框架【%s】$' % (mode_pvs))
def scrollToDown(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.forward()
    d.wait.idle()
    
@step(u'手指向下滚动框架【%s】$' % (mode_pvs))
def scrollToDown(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.backward()
    d.wait.idle()
    
# 步长
@step(u'以步长【%s】手指向左滚动框架【%s】$' % (mode_int, mode_pvs))
def scrollLeftByStep(step, stepcond, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.forward(steps=stepcond)
    d.wait.idle()

@step(u'以步长【%s】手指向右滚动框架【%s】$' % (mode_int, mode_pvs))
def scrollRightByStep(step, stepcond, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.backward(steps=stepcond)
    d.wait.idle()

@step(u'以步长【%s】手指向上滚动框架【%s】$' % (mode_int, mode_pvs))
def scrollUpByStep(step, stepcond, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.forward(steps=stepcond)
    d.wait.idle()
    
@step(u'以步长【%s】手指向下滚动框架【%s】$' % (mode_int, mode_pvs))
def scrollDownByStep(step, stepcond, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.backward(steps=stepcond)
    d.wait.idle()
    
# 到起始/结束位置
@step(u'手指向左边起始位置滚动框架【%s】$' % (mode_pvs))
def scrollHorizToEnd(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.toEnd()
    d.wait.idle()
    
@step(u'手指向右边结束位置滚动框架【%s】$' % (mode_pvs))
def scrollHorizToBegin(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.horiz.toBeginning()
    d.wait.idle()

@step(u'手指向上边起始位置滚动框架【%s】$' % (mode_pvs))
def scrollVertToEnd(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.toEnd()
    d.wait.idle()

@step(u'手指向下边结束位置滚动框架【%s】$' % (mode_pvs))
def scrollVertToBegin(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).scroll.vert.toBeginning()
    d.wait.idle()

'''
滚动至XX位置
'''
# 到页面元素位置
@step(u'手指纵向滚动至页面元素【%s】$' % (mode_pvs))
def scrollVertFind(step, cond):
    dict = get_dict_from_cond(cond)
    d().scroll.vert.to(**dict)

@step(u'手指横向滚动至页面元素【%s】$' % (mode_pvs))
def scrollhorizFind(step, cond):
    dict = get_dict_from_cond(cond)
    d().scroll.horiz.to(**dict)
    
# 到页面文本(text、description)位置
@step(u'手指纵向滚动至文本【%s】$' % (mode_text))
def scrollVertFind(step, cond):
    dict = get_dict_from_cond(cond)
    d().scroll.vert.to(text=cond)
    
@step(u'手指横向滚动至文本【%s】$' % (mode_text))
def scrollhorizFind(step, cond):
    dict = get_dict_from_cond(cond)
    d().scroll.horiz.to(text=cond)
     
# 到某页面元素位置
@step(u'手指纵向滚动框架【%s】至页面元素【%s】$' % (mode_pvs,mode_pvs))
def scrollVertFind(step, scrollcond, element):
    elements = get_dict_from_cond(scrollcond)
    pageElement = get_dict_from_cond(element)
    d(**elements).scroll.vert.to(**pageElement)

@step(u'手指横向滚动框架【%s】至页面元素【%s】$' % (mode_pvs,mode_pvs))
def scrollhorizFind(step, scrollcond, element):
    elements = get_dict_from_cond(scrollcond)
    pageElement = get_dict_from_cond(element)
    d(**elements).scroll.horiz.to(**pageElement)
     
# 到某页面text位置
@step(u'手指纵向滚动框架【%s】至文本【%s】$' % (mode_pvs,mode_text))
def scrollVertFind(step, scrollcond, textcond):
    elements = get_dict_from_cond(scrollcond)
    d(**elements).scroll.vert.to(text=textcond)

@step(u'手指横向滚动框架【%s】至文本【%s】$' % (mode_pvs,mode_text))
def scrollhorizFind(step, scrollcond, textcond):
    elements = get_dict_from_cond(scrollcond)
    d(**elements).scroll.horiz.to(text=textcond)
    
# 到某页面description位置
@step(u'手指纵向滚动框架【%s】至文本描述【%s】$' % (mode_pvs,mode_text))
def scrollVertFind(step, scrollcond, desccond):
    elements = get_dict_from_cond(scrollcond)
    d(**elements).scroll.vert.to(description=desccond)

@step(u'手指横向滚动框架【%s】至文本描述【%s】$' % (mode_pvs,mode_text))
def scrollhorizFind(step, scrollcond, desccond):
    elements = get_dict_from_cond(scrollcond)
    d(**elements).scroll.horiz.to(description=desccond)
