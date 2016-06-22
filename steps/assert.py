# -*- coding: utf-8 -*- 
import re
import sys
from lettuce import *
import compimg
from lettuce.regex import *
from uiautomator.myDevice import device as d  
    
@step(u'应该可看到页面元素【%s】$' % (mode_pvs))
def assertElementsExist(step, cond):
    element = get_dict_from_cond(cond)
    assert d(**element).exists
    d.wait.idle()
    
@step(u'应该看不到页面元素【%s】$' % (mode_pvs))
def assertElementsGone(step, cond):
    element = get_dict_from_cond(cond)
    assert not d(**element).exists
    d.wait.idle()
    
@step(u'页面元素【%s】的数量应该为【%s】$' % (mode_pvs, mode_int))
def countElement(step, cond, count):
    elements = get_dict_from_cond(cond)
    assert d(**elements).count==int(count)
    d.wait.idle()

@step(u'等待更新超时时间【%s】毫秒后，包为【%s】的页面应该更新$' % (mode_int,mode_text))
def waitForUpdate(step, time, cond):
    assert d.wait.update(timeout=time,package_name=cond)  

@step(u'等待，页面元素【%s】应该消失$' % (mode_pvs))
def waitGone(step, cond):
    elements = get_dict_from_cond(cond)
    assert d(**elements).wait.gone() 
    
@step(u'在【%s】毫秒内，页面元素【%s】应该消失$' % (mode_int, mode_pvs))
def waitGone(step, time, cond):
    elements = get_dict_from_cond(cond)
    assert d(**elements).wait.gone(timeout=time)   
    
@step(u'等待，页面元素【%s】应该出现$' % (mode_pvs))
def waitGone(step, cond):
    elements = get_dict_from_cond(cond)
    assert d(**elements).wait.exists() 
    
@step(u'在【%s】毫秒内，页面元素【%s】应该出现$' % (mode_int, mode_pvs))
def waitGone(step, time, cond):
    elements = get_dict_from_cond(cond)
    assert d(**elements).wait.exists(timeout=time) 
    

#应该看到页面text
@step(u'应该可看到文本【%s】$' % (mode_text))
def assertElementsExist(step, textcond):
    assert d(text=textcond).exists
    d.wait.idle()

#应该看不到页面text  
@step(u'应该看不到文本【%s】$' % (mode_text))
def assertElementsGone(step, textcond):
    assert not d(text=textcond).exists
    d.wait.idle()
    
#应该看到页面description
@step(u'应该可找到文本描述【%s】$' % (mode_text))
def assertElementsExist(step, desccond):
    assert d(description=desccond).exists
    d.wait.idle()

#应该看不到页面description  
@step(u'应该找不到文本描述【%s】$' % (mode_text))
def assertElementsGone(step, desccond):
    assert not d(description=desccond).exists
    d.wait.idle()
    
#页面上的text应该消失    
@step(u'等待，文本【%s】应该消失$' % (mode_text))
def waitGone(step, cond):
    assert d(text=cond).wait.gone() 
    
#页面上的description应该消失    
@step(u'等待，文本描述【%s】应该找不到$' % (mode_text))
def waitGone(step, cond):
    assert d(description=cond).wait.gone() 
 
#等待后，页面元素text消失 
@step(u'在【%s】毫秒内，文本【%s】应该消失$' % (mode_int, mode_text))
def waitGone(step, time, cond):
    assert d(text=cond).wait.gone(timeout=time)   

#等待后，页面元素description消失 
@step(u'在【%s】毫秒内，文本描述【%s】应该找不到$' % (mode_int, mode_text))
def waitGone(step, time, cond):
    assert d(description=cond).wait.gone(timeout=time)     

#等待页面元素text出现    
@step(u'等待，文本【%s】应该出现$' % (mode_text))
def waitGone(step, cond):
    assert d(text=cond).wait.exists() 
    
#等待页面元素description出现    
@step(u'等待，文本描述【%s】应该被找到$' % (mode_text))
def waitGone(step, cond):
    assert d(description=cond).wait.exists() 
    
#等待时间后，text出现
@step(u'在【%s】毫秒内，文本【%s】应该出现$' % (mode_int, mode_text))
def waitGone(step, time, cond):
    assert d(text=cond).wait.exists(timeout=time)
    
#等待时间后，description出现
@step(u'在【%s】毫秒内，文本描述【%s】应该被找到$' % (mode_int, mode_text))
def waitGone(step, time, cond):
    assert d(description=cond).wait.exists(timeout=time)
    
#比较图片是否相等
#误差值不大于百分之【1】
@step(u'图片【%s】与模板图片【%s】对比，误差不大于百分之【%s】$' % (mode_file,mode_file,mode_int))
def compareImg(step, subPathcond, srcPathcond, thresholdcond):
    assert comparison.isMatch(subPathcond, srcPathcond, float(thresholdcond)/100)