# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d    

@before_feature_of(u"1通话-1使用2G卡通话") # provide your feature name here
def before_clear_call_logs(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        ex.start_activity("com.android.dialer/com.android.dialer.DialtactsActivity")
        d(description="通话记录").click.wait()
        if d(text="没有通话记录。").exists:
            return None 
        d.press("menu")
        d(text="删除").click.wait()
        d(resourceId="com.android.dialer:id/select_items").click.wait()
        d(text="全选").click.wait()
        d(text="确定").click.wait()
        if d(text="删除通话记录？").exists:
            d(text="确定").click.wait()
        assert not d(text="没有通话记录。").exists
    except:
        None
    

@after_feature_of(u"1通话-1使用2G卡通话") # provide your feature name here
def after_clear_call_logs(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        ex.start_activity("com.android.dialer/com.android.dialer.DialtactsActivity")
        d(description="通话记录").click.wait()
        if d(text="没有通话记录。").exists:
            return None 
        d.press("menu")
        d(text="删除").click.wait()
        d(resourceId="com.android.dialer:id/select_items").click.wait()
        d(text="全选").click.wait()
        d(text="确定").click.wait()
        if d(text="删除通话记录？").exists:
            d(text="确定").click.wait()
        assert not d(text="没有通话记录。").exists
    except:
        None
    