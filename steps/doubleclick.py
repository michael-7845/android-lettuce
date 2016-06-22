# -*- coding: utf-8 -*- 
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

@step(u'快速双击页面元素【%s】$' % (mode_pvs))
def double_click(step, condition):
    dict = get_dict_from_cond(condition)
    d(**dict).click()
    d(**dict).click()
    d.wait.update()

# *-* 坐标，强烈不建议使用 *-*
@step(u'快速双击页面坐标【%s】$' % (mode_position))
def long_click_x_y(step, x, y):
    d.click(int(x), int(y))
    d.click(int(x), int(y))
    d.wait.update()
