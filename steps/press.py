# -*- coding: utf-8 -*- 
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

''' 说明：
1. 支持的物理键名字
home, HOME键
back, 回退键
left, 导向左键
right, 导向右键
up, 导向上键
down, 导向下键
center, 导向居中键
menu,  菜单键
search, 搜索键
enter, 回车键
delete(or del), 删除键 
recent(recent apps), 最近使用APP键
volume_up, 音量+键
volume_down, 音量-键
volume_mute, 静音键
camera, 拍照键
power, 电源键
2. 键码定义
http://blog.csdn.net/feizhixuan46789/article/details/16801429
'''

# *-* 点按 *-*
@step(u'点按物理键【%s】$' % (mode_word))
def press_key(step, key):
    d.press(key)
    d.wait.update()
    
@step(u'点按键码【%s】$' % (mode_keycode))
def press_keycode(step, keycode):
    print keycode
    kc = int(keycode,16)
    d.press(kc)
    d.wait.update()
    
# *-* 快速双按 *-*
@step(u'快速双按物理键【%s】$' % (mode_word))
def double_press_key(step, key):
    d.press(key)
    d.press(key)
    d.wait.update()
    
@step(u'快速双按键码【%s】$' % (mode_keycode))
def double_press_keycode(step, keycode):
    kc = int(keycode,16)
    d.press(kc)
    d.press(kc)
    d.wait.update()

# *-* 同时点按 *-*
@step(u'同时点按键码【%s】和【%s】$' % (mode_keycode, mode_keycode))
def press_2_key(step, keycode1, keycode2):
    kc1 = int(keycode1,16)
    kc2 = int(keycode2,16)
    d.press(kc1, kc2)
    d.wait.update()
