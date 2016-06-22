# -*- coding: utf-8 -*- 
from lettuce import *
from uiautomator.myDevice import device as d
from lettuce.regex import *

''' 说明：
1. 页面元素的可用属性列表
text, 属性text等于
textContains, 属性text包含
textMatches, 属性text匹配
textStartsWith, 属性text以此开始
className, 属性className等于
classNameMatches, 属性className匹配
description, 属性content-desc等于
descriptionContains, 属性content-desc包含
descriptionMatches, 属性content-desc匹配
descriptionStartsWith, 属性description以此开始
checkable, 属性checkable等于true/false(不能写作True/False)
checked, 属性checked等于true/false(不能写作True/False)
clickable, 属性clickable等于true/false(不能写作True/False)
longClickable, 属性longClickable等于true/false(不能写作True/False)
scrollable, 属性scrollable等于true/false(不能写作True/False)
enabled, 属性enabled等于true/false(不能写作True/False)
focusable, 属性focusable等于true/false(不能写作True/False)
focused, 属性focused等于true/false(不能写作True/False)
selected, 属性selected等于true/false(不能写作True/False)
packageName, 属性packageName等于
packageNameMatches, 属性packageName匹配
resourceId, 属性resourceId等于
resourceIdMatches, 属性resourceId匹配
index, 属性index等于
instance, 第几个实例
'''

@step(u'长按页面元素【%s】$' % (mode_pvs))
def long_click(step, condition):
    dict = get_dict_from_cond(condition)
    d(**dict).long_click()
    d.wait.update()
    
@step(u'长按页面元素，父【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_child(step, cond, childcond):
    father = get_dict_from_cond(cond)
    child = get_dict_from_cond(childcond)
    d(**father).child(**child).long_click()
    d.wait.update()

@step(u'长按页面元素，兄【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_sibling(step, siblingcond, cond):
    sibling = get_dict_from_cond(siblingcond)
    my = get_dict_from_cond(cond)
    d(**sibling).sibling(**my).long_click()
    d.wait.update()
    
@step(u'长按【%s】上边的【%s】页面元素$' % (mode_pvs, mode_pvs))
def long_click_up(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).up(**my).long_click()
    d.wait.update()

@step(u'长按【%s】下边的【%s】页面元素$' % (mode_pvs, mode_pvs))
def long_click_down(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).down(**my).long_click()
    d.wait.update()

@step(u'长按【%s】左边的【%s】页面元素$' % (mode_pvs, mode_pvs))
def long_click_left(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).left(**my).long_click()
    d.wait.update()
    
@step(u'长按【%s】右边的【%s】页面元素$' % (mode_pvs, mode_pvs))
def long_click_right(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).right(**my).long_click()
    d.wait.update()

# *-* 坐标，强烈不建议使用 *-*
@step(u'长按页面坐标【%s】$' % (mode_position))
def long_click_x_y(step, x, y):
    d.long_click(int(x), int(y))
    d.wait.update()

# *-* 在可滚动的框架中查找 *-*
# *-* 未提供点击左上角或右下角功能语句 *-*
# 简约写法
@step(u'长按可滚动框架【%s】内的特征文字【%s】页面元素$' % (mode_pvs, mode_text))
def click_child_by_text(step, scrollcond, trait):
    scroll = get_dict_from_cond(scrollcond)
    d(**scroll).child_by_text(trait,allow_scroll_search=True,textContains=trait).long_click()
    d.wait.update()

@step(u'长按可滚动框架【%s】内的特征描述【%s】页面元素$' % (mode_pvs, mode_text))
def click_child_by_desc(step, scrollcond, trait):
    scroll = get_dict_from_cond(scrollcond)
    d(**scroll).child_by_description(trait,allow_scroll_search=True,descriptionContains=trait).long_click()
    d.wait.update()

@step(u'长按可滚动框架【%s】内的特征序号【%s】页面元素$' % (mode_pvs, mode_int))
def click_child_by_inst(step, framecond, trait):
    frame = get_dict_from_cond(framecond)
    d(**frame).child_by_instance(trait,instance=trait).long_click()
    d.wait.update()

# 完备写法
@step(u'长按可滚动框架【%s】内的页面元素【%s】且其子孙结点含text值【%s】$' % (mode_pvs, mode_pvs, mode_text))
def long_click_child_by_text(step, scrollcond, cond, text):
    scroll = get_dict_from_cond(scrollcond)
    my = get_dict_from_cond(cond)
    d(**scroll).child_by_text(text,allow_scroll_search=True,**my).long_click()
    d.wait.update()

@step(u'长按可滚动框架【%s】内的页面元素【%s】且其子孙结点含description值【%s】$' % (mode_pvs, mode_pvs, mode_text))
def long_click_child_by_desc(step, scrollcond, cond, desc):
    scroll = get_dict_from_cond(scrollcond)
    my = get_dict_from_cond(cond)
    d(**scroll).child_by_description(desc,allow_scroll_search=True,**my).long_click()
    d.wait.update()

#未提供长按左上角或右下角功能语句
@step(u'在框架【%s】内，长按页面元素【%s】且子孙结点含instance序号【%s】$' % (mode_pvs, mode_pvs, mode_int))
def long_click_child_by_inst(step, framecond, cond, inst):
    frame = get_dict_from_cond(framecond)
    my = get_dict_from_cond(cond)
    d(**frame).child_by_instance(inst,**my).long_click()
    d.wait.update()

# *-* 左上角 *-*
@step(u'长按页面元素左上角【%s】$' % (mode_pvs))
def long_click_tl(step, condition):
    dict = get_dict_from_cond(condition)
    d(**dict).long_click.topleft()
    d.wait.update()

@step(u'长按页面元素左上角，父【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_child_tl(step, cond, childcond):
    father = get_dict_from_cond(cond)
    child = get_dict_from_cond(childcond)
    d(**father).child(**child).long_click.topleft()
    d.wait.update()

@step(u'长按页面元素左上角，兄【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_sibling_tl(step, siblingcond, cond):
    sibling = get_dict_from_cond(siblingcond)
    my = get_dict_from_cond(cond)
    d(**sibling).sibling(**my).long_click.topleft()
    d.wait.update()
    
@step(u'长按【%s】上边的【%s】页面元素左上角$' % (mode_pvs, mode_pvs))
def long_click_up_tl(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).up(**my).long_click.topleft()
    d.wait.update()

@step(u'长按【%s】下边的【%s】页面元素左上角$' % (mode_pvs, mode_pvs))
def long_click_down_tl(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).down(**my).long_click.topleft()
    d.wait.update()

@step(u'长按【%s】左边的【%s】页面元素左上角$' % (mode_pvs, mode_pvs))
def long_click_left_tl(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).left(**my).long_click.topleft()
    d.wait.update()
    
@step(u'长按【%s】右边的【%s】页面元素左上角$' % (mode_pvs, mode_pvs))
def long_click_right_tl(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).right(**my).long_click.topleft()
    d.wait.update()

# *-* 右下角 *-*
@step(u'长按页面元素右下角【%s】$' % (mode_pvs))
def long_click_br(step, condition):
    dict = get_dict_from_cond(condition)
    d(**dict).long_click.bottomright()
    d.wait.update()

@step(u'长按页面元素右下角，父【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_child_br(step, cond, childcond):
    father = get_dict_from_cond(cond)
    child = get_dict_from_cond(childcond)
    d(**father).child(**child).long_click.bottomright()
    d.wait.update()

@step(u'长按页面元素右下角，兄【%s】自【%s】$' % (mode_pvs, mode_pvs))
def long_click_sibling_br(step, siblingcond, cond):
    sibling = get_dict_from_cond(siblingcond)
    my = get_dict_from_cond(cond)
    d(**sibling).sibling(**my).long_click.bottomright()
    d.wait.update()
    
@step(u'长按【%s】上边的【%s】页面元素右下角$' % (mode_pvs, mode_pvs))
def long_click_up_br(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).up(**my).long_click.bottomright()
    d.wait.update()

@step(u'长按【%s】下边的【%s】页面元素右下角$' % (mode_pvs, mode_pvs))
def long_click_down_br(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).down(**my).long_click.bottomright()
    d.wait.update()

@step(u'长按【%s】左边的【%s】页面元素右下角$' % (mode_pvs, mode_pvs))
def long_click_left_br(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).left(**my).long_click.bottomright()
    d.wait.update()
    
@step(u'长按【%s】右边的【%s】页面元素右下角$' % (mode_pvs, mode_pvs))
def long_click_right_br(step, reference, cond):
    ref = get_dict_from_cond(reference)
    my = get_dict_from_cond(cond)
    d(**ref).right(**my).long_click.bottomright()
    d.wait.update()
