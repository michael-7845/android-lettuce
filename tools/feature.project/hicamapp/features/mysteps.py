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

@step(u'应该可以看见页面元素父【%s】子【%s】自【%s】的文本为【%s】$' % (mode_pvs,mode_pvs,mode_pvs,mode_text))
def father_child_self_text(step, fathercond, childcond, selfscond, textcond):
    father = get_dict_from_cond(fathercond)
    child = get_dict_from_cond(childcond)
    selfs = get_dict_from_cond(selfscond)
    assert d(**father).child(**child).child(**selfs).child(text=textcond).exists

@step(u'应该可以看见页面元素父【%s】子【%s】自【%s】$' % (mode_pvs,mode_pvs,mode_pvs))
def father_child_self_text(step, fathercond, childcond, selfscond):
    father = get_dict_from_cond(fathercond)
    child = get_dict_from_cond(childcond)
    selfs = get_dict_from_cond(selfscond)
    assert d(**father).child(**child).child(**selfs).exists