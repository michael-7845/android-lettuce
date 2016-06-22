# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
from uiautomator.myDevice import device2 as d2
'''
Messaging callback
'''        
@before_scenario_in_feature_of(u"2短信-1使用2G卡") # provide your feature name here
def before_clear_message(scenario):
   # adding the operation before <each scenario> of <this feature>
    print "@before scenario"
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        ex.start_activity("com.android.mms/com.android.mms.ui.ConversationList")
        if d(text="无会话").exists:
            return None 
        d.press("menu")
        d(text="删除所有会话").click.wait()
        if d(text="将会删除所有会话。").exists:
            #d(text="删除").click.wait()不执行
            d(resourceId="android:id/button1").click.wait()
        assert not d(text="无会话").exists
    except:
        None

@after_scenario_in_feature_of(u"2短信-1使用2G卡") # provide your feature name here
def after_clear_message(scenario):
    print "@after scenario"
    # adding the operation after <each scenario> of <this feature>
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        ex.start_activity("com.android.mms/com.android.mms.ui.ConversationList")
        if d(text="无会话").exists:
            return None 
        d.press("menu")
        d(text="删除所有会话").click.wait()
        if d(text="将会删除所有会话。").exists:
            #d(text="删除").click.wait()不执行
            d(resourceId="android:id/button1").click.wait()
        assert not d(text="无会话").exists
        d.press("home")
    except:
        None    