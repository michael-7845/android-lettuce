# -*- coding: utf-8 -*- 
from lettuce import *

from lettuce.regex import *
from uiautomator.myDevice import device as d

# as your need, define your own steps
@step(u'点按物理键【%s】【%s】次$' % (mode_word, mode_int))
def press_many_times(step, key, times):
    times= int(times)
    time = 0
    while times > time:
        d.press(key)
        d.wait.update()
        time += 1
        
@step(u'应该可看到页面元素父【%s】自【%s】$' % (mode_pvs, mode_pvs))
def assertElementsGone(step, cond, childcond):
    father = get_dict_from_cond(cond)
    child = get_dict_from_cond(childcond)
    assert d(**father).child(**child).exists
    d.wait.idle()