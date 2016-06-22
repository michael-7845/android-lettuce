# -*- coding: utf-8 -*- 
# swipe 滑动
# drag 拖动
# fling 快速滑动
# scroll 滚动
# notes : drag can not be set until Android 4.3.
import re,sys
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

@step(u'从坐标【%s】拖动至坐标【%s】$' % (mode_position, mode_position))
def dragXtoY(step, x1, y1, x2, y2):
    d.drag(x1,y1,x2,y2)
    d.wait.idle()

@step(u'以步长【%s】从坐标【%s】拖动至坐标【%s】$' % (mode_int, mode_position, mode_position))
def dragXtoY(step, steps, x1, y1, x2, y2):
    d.drag(x1,y1,x2,y2,steps)
    d.wait.idle()
    
@step(u'拖动页面元素【%s】至坐标【%s】$' % (mode_pvs, mode_position))
def dragObjTo(step, cond, x, y):
    obj = get_dict_from_cond(cond)
    d(**obj).drag.to(x,y)
    d.wait.idle()

@step(u'以步长【%s】拖动页面元素【%s】到坐标【%s】$' % (mode_int, mode_pvs, mode_position))
def dragObjToByStep(step, steps, cond, x, y):
    obj = get_dict_from_cond(cond)
    d(**obj).drag.to(x,y,steps)  
    d.wait.idle()    

@step(u'拖动页面元素【%s】至页面元素【%s】$' % (mode_pvs, mode_pvs))
def dragObjToObj(step, cond, cond1):
    obj = get_dict_from_cond(cond)
    obj1 = get_dict_from_cond(cond1)
    d(**obj).drag.to(**obj1)
    d.wait.idle()

#拖动text至坐标点
@step(u'拖动文本【%s】至坐标【%s】$' % (mode_text, mode_position))
def dragObjTo(step, cond, x, y):
    d(text=cond).drag.to(x,y)
    d.wait.idle()

#拖动description至坐标点
@step(u'拖动文本描述【%s】至坐标【%s】$' % (mode_text, mode_position))
def dragObjTo(step, cond, x, y):
    d(description=cond).drag.to(x,y)
    d.wait.idle()

#拖动text至另一个text
@step(u'拖动文本【%s】至另一个文本【%s】$' % (mode_text, mode_text))
def dragObjToObj(step, fromtext, totext):
    d(text=fromtext).drag.to(text=totext)
    d.wait.idle()
    
#拖动description至一个text
@step(u'拖动文本描述【%s】至一个文本【%s】$' % (mode_text, mode_text))
def dragObjToObj(step, fromdesc, totext):
    d(description=fromdesc).drag.to(text=totext)
    d.wait.idle()
    
#拖动description至另一个description
@step(u'拖动文本描述【%s】至另一个文本描述【%s】$' % (mode_text, mode_text))
def dragObjToObj(step, fromdesc, todesc):
    d(description=fromdesc).drag.to(description=todesc)
    d.wait.idle()
    
#拖动text至一个description
@step(u'拖动文本【%s】至一个文本描述【%s】$' % (mode_text, mode_text))
def dragObjToObj(step, fromtext, todesc):
    d(text=fromtext).drag.to(description=todesc)
    d.wait.idle()