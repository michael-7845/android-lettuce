# -*- coding: utf-8 -*- 
# swipe 滑动
# drag 拖动
# fling 快速滑动
# scroll 滚动
import re,sys
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

@step(u'手指向左滑动屏幕$')
def swipeLeft(step):
    d().swipe("left")
    d.wait.idle()

@step(u'手指向右滑动屏幕$')
def swipeRight(step):
    d().swipe("right")
    d.wait.idle()
    
@step(u'手指向上滑动屏幕$')
def swipeUp(step):
    d().swipe("up")  
    d.wait.idle()    

@step(u'手指向下滑动屏幕$')
def swipeDown(step):
    d().swipe("down")
    d.wait.idle()

@step(u'手指以步长【%s】向左滑动屏幕$' % (mode_int))
def swipeLeftByStep(step, number):
    d().swipe("left", number)
    d.wait.idle()

@step(u'手指以步长【%s】向右滑动屏幕$' % (mode_int))
def swipeRightByStep(step, number):
    d().swipe("right", number)
    d.wait.idle()

@step(u'手指以步长【%s】向上滑动屏幕$' % (mode_int))
def swipeUpByStep(step, number):
    d().swipe("up", number)
    d.wait.idle()

@step(u'手指以步长【%s】向下滑动屏幕$' % (mode_int))
def swipeDownByStep(step, number):
    d().swipe("down", number)
    d.wait.idle()

@step(u'手指从坐标【%s】滑动至坐标【%s】$' % (mode_position, mode_position))
def swipeXtoY(step,x1,y1,x2,y2):
    d.swipe(x1,y1,x2,y2)
    d.wait.idle()
    
@step(u'手指以步长【%s】从坐标【%s】滑动至坐标【%s】$' % (mode_int,mode_position,mode_position))
def swipeXtoY(step,steps,x1,y1,x2,y2):
    d.swipe(x1,y1,x2,y2,steps)
    d.wait.idle()

@step(u'以页面元素【%s】为范围，手指从右向左滑动$' % (mode_pvs))
def swipeTxt2Left(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).swipe.left()
    d.wait.idle()

@step(u'以页面元素【%s】为范围，手指从左向右滑动$' % (mode_pvs))
def swipeTxt2Right(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).swipe.right()
    d.wait.idle()
    
@step(u'以页面元素【%s】为范围，手指从下向上滑动$' % (mode_pvs))
def swipeTxt2Up(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).swipe.up()
    d.wait.idle()

@step(u'以页面元素【%s】为范围，手指从上向下滑动$' % (mode_pvs))
def swipeTxt2Down(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).swipe.down()
    d.wait.idle()

@step(u'以页面元素【%s】为范围，步长为【%s】手指从右向左滑动$' % (mode_pvs,mode_int))
def swipeTxt2LeftByStep(step, cond, stepcond):
    text = get_dict_from_cond(cond)
    d(**text).swipe.left(steps=stepcond)
    d.wait.idle()

@step(u'以页面元素【%s】为范围，步长为【%s】手指从左向右滑动$' % (mode_pvs,mode_int))
def swipeTxt2RightByStep(step, cond, stepcond):
    text = get_dict_from_cond(cond)
    d(**text).swipe.right(steps=stepcond)
    d.wait.idle()
    
@step(u'以页面元素【%s】为范围，步长为【%s】手指从下向上滑动$' % (mode_pvs,mode_int))
def swipeTxt2UpByStep(step, cond, stepcond):
    text = get_dict_from_cond(cond)
    d(**text).swipe.up(steps=stepcond)
    d.wait.idle()

@step(u'以页面元素【%s】为范围，步长为【%s】手指从上向下滑动$' % (mode_pvs,mode_int))
def swipeTxt2DownByStep(step, cond, stepcond):
    text = get_dict_from_cond(cond)
    d(**text).swipe.down(steps=stepcond)
    d.wait.idle()

    
#以text为范围（文本中含有空格）
@step(u'以文本【%s】为范围，手指从右向左滑动$' % (mode_text))
def swipeTxt2Left(step, cond):
    d(text=cond).swipe.left()
    d.wait.idle()

@step(u'以文本【%s】为范围，手指从左向右滑动$' % (mode_text))
def swipeTxt2Right(step, cond):
    elements = get_dict_from_cond(cond)
    d(text=cond).swipe.right()
    d.wait.idle()
    
@step(u'以文本【%s】为范围，手指从下向上滑动$' % (mode_text))
def swipeTxt2Up(step, cond):
    d(text=cond).swipe.up()
    d.wait.idle()

@step(u'以文本【%s】为范围，手指从上向下滑动$' % (mode_text))
def swipeTxt2Down(step, cond):
    elements = get_dict_from_cond(cond)
    d(text=cond).swipe.down()
    d.wait.idle()
    
#以description为范围（文本中含有空格）
@step(u'以文本描述【%s】为范围，手指从右向左滑动$' % (mode_text))
def swipeTxt2Left(step, cond):
    d(description=cond).swipe.left()
    d.wait.idle()

@step(u'以文本描述【%s】为范围，手指从左向右滑动$' % (mode_text))
def swipeTxt2Right(step, cond):
    d(description=cond).swipe.right()
    d.wait.idle()
    
@step(u'以文本描述【%s】为范围，手指从下向上滑动$' % (mode_text))
def swipeTxt2Up(step, cond):
    d(description=cond).swipe.up()
    d.wait.idle()

@step(u'以文本描述【%s】为范围，手指从上向下滑动$' % (mode_text))
def swipeTxt2Down(step, cond):
    d(description=cond).swipe.down()
    d.wait.idle()