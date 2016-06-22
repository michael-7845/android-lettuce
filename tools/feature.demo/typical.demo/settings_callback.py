# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
    
@before_feature_of(u"3设置-1修改设置") # provide your feature name here
def before_reset(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        #reset screen locked
        ex.start_activity("com.android.settings/.Settings")
        d(className="android.widget.ListView").scroll.vert.to(text="安全")
        d(text="安全").click.wait()
        if d(text="滑动").exists:
            d.press("back")
        else:
            d(text="屏幕锁定").click.wait()
            d(text="滑动").click.wait()
            #assert not d(text="滑动").exists(timeout=3000)
            d.press("back")  
        
        #reset schedule power
        d(className="android.widget.ListView").scroll.vert.to(text="定时开关机")
        d(text="定时开关机").click.wait()
        
        if d(className="android.widget.ListView").child(className="android.widget.LinearLayout",index=0).child(className="android.widget.CheckBox",checked=False).exists:
            d.press("back")
        else:
            d(text="07:00").right(className="android.widget.CheckBox").click.wait()
            d.press("back")  
        
        #reset auto-rotate screen
        d(className="android.widget.ListView").scroll.vert.to(text="显示")
        d(text="显示").click.wait()
        if d(className="className=android.widget.LinearLayout",index=7).child(className="android.widget.CheckBox",checked=False).exists:
            d.press("back")  
        else:
            d(text="自动旋转屏幕").right(className="android.widget.CheckBox").click.wait()
            d.press("back")  
    except Exception as e:
        print e
    

@after_feature_of(u"3设置-1修改设置") # provide your feature name here
def after_recovery(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        ex.start_activity("com.android.settings/.Settings")
        #reset screen locked
        d(className="android.widget.ListView").scroll.vert.to(text="安全")
        d(text="安全").click.wait()
        if d(text="滑动").exists:
            d.press("back")
        else:
            d(text="屏幕锁定").click.wait()
            d(text="滑动").click.wait()
            #assert not d(text="滑动").exists(timeout=3000)
            d.press("back")  
        
        #reset schedule power
        d(className="android.widget.ListView").scroll.vert.to(text="定时开关机")
        d(text="定时开关机").click.wait()
        if d(className="android.widget.ListView").child(className="android.widget.LinearLayout",index=0).child(className="android.widget.CheckBox",checked=False).exists:
            d.press("back")
        else:
            d(text="07:00").right(className="android.widget.CheckBox").click.wait()
            d.press("back")
        
        #reset auto-rotate screen
        d(className="android.widget.ListView").scroll.vert.to(text="显示")
        d(text="显示").click.wait()
        if d(className="android.widget.LinearLayout",index=7).child(className="android.widget.CheckBox",checked=False).exists:
            d.press("back")
        else:
            d(text="自动旋转屏幕").right(className="android.widget.CheckBox").click.wait()
            d.press("back")  
        #return home
        d.press("home")
    except:
        None

@before_scenario_in_feature_of(u"3设置-1修改设置") # provide your feature name here
def before_clear_message(scenario):
   # adding the operation before <each scenario> of <this feature>
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@after_scenario_in_feature_of(u"3设置-1修改设置") # provide your feature name here
def after_clear_message(scenario):
    # adding the operation after <each scenario> of <this feature>
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")