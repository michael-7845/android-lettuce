# -*- coding: utf-8 -*- 
import re
import sys
import time
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

#作者提供的 False为un-freeze rotation有误
#Fasle为打开自动旋转，默认为关闭自动旋转
@step(u'打开自动旋转屏幕$')
def freezeRotation(step):
    d.freeze_rotation(False)
    d.wait.idle()

@step(u'关闭自动旋转屏幕$')
def freezeRotation(step):
    d.freeze_rotation()
    d.wait.idle()    

@step(u'点亮屏幕$')
def screenon(step):
    d.screen.on()
    d.wait.idle()  

@step(u'熄灭屏幕$')
def screenoff(step):
    d.screen.off()
    d.wait.idle()  
    
#保存.xml到相对路径
#用法举例:
#保存在当前lettuce执行目录下,文件名字为layout.xml
# 下载界面结构文件保存为【layout.xml】
# 下载界面结构文件保存为【./layout.xml】
#保存在当前lettuce执行目录下的tools目录下,文件名字为layout.xml
# 下载界面结构文件保存为【tools/layout.xml】
# 下载界面结构文件保存为【./tools/layout.xml】
@step(u'下载界面结构文件保存为【%s】$' % (mode_text))
def dumpHierarchy(step,path):
    d.dump(path)
    d.wait.idle()  

# open notification, can not work until Android 4.3.  
@step(u'打开通知栏$')
def oepnNotification(step):
    d.open("notification")
    d.wait.idle()  

# open quick settings, can not work until Android 4.3.    
@step(u'打开快速设置$')
def oepnQuickSetting(step):
    d.open.quick_settings()
    d.wait.idle()
    
@step(u'等待窗口空闲$')
def waitForIdle(step):
    d.wait.idle()

@step(u'等待窗口空闲超时时间【%s】毫秒$' % (mode_int))
def waitForIdle(step, time):
    d.wait.idle(timeout=time)

#支持页面元素resourceId等
@step(u'清除页面元素【%s】中的文字$' % (mode_pvs))
def clearTextField(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).clear_text()  
    d.wait.idle()

@step(u'在页面元素【%s】添加文本【%s】$' % (mode_pvs, mode_text))
def setText(step, cond, text):
    elements = get_dict_from_cond(cond)
    d(**elements).set_text(text)
    d.wait.idle()
    
@step(u'从两点【%s】和【%s】分别滑动至另外两点【%s】和【%s】$' % (mode_position,mode_position,mode_position,mode_position))
def gesture(step, sx1, sy1, sx2, sy2, ex1, ey1, ex2, ey2):
    d(className="android.widget.EditText").gesture((sx1, sy1), (sx2, sy2)) \
                  .to((ex1, ey1), (ex2, ey2))   
    d.wait.idle()
    
# notes : pinch can not be set until Android 4.3.
@step(u'从左右边缘同时滑向中心$')
def pinchIn(step):
    d().pinch.In(percent=100, steps=10)
    d.wait.idle()

@step(u'从中心同时滑向左右两边$')
def pinchOut(step):
    d().pinch.Out(percent=100, steps=10)
    d.wait.idle()

@step(u'分别以左右距边缘位置百分之【%s】处，按照步长【%s】同时滑向中心$' % (mode_int,mode_int))
def pinchIn(step, per, stepcond):
    d().pinch.In(percent=per,steps=stepcond)
    d.wait.idle()

@step(u'从中心以步长【%s】同时滑向左右距边缘位置百分之【%s】处$' % (mode_int,mode_int))
def pinchOut(step, stepcond, per):
    d().pinch.Out(percent=per,steps=stepcond)
    d.wait.idle()
    
@step(u'以页面元素【%s】为范围，从左右边缘同时滑向中心$' % (mode_pvs))
def pinchIn(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).pinch.In(percent=100, steps=10)
    d.wait.idle()

@step(u'以页面元素【%s】为范围，从中心同时滑向左右两边$' % (mode_pvs))
def pinchOut(step, cond):
    elements = get_dict_from_cond(cond)
    d(**elements).pinch.Out(percent=100, steps=10)
    d.wait.idle()
    
@step(u'等待【%s】毫秒，不做任何操作$' % (mode_int))
def silent_wait(step, millisec):
    sec = (float(millisec))/1000
    time.sleep(sec)
    