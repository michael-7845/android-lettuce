# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d

@before_feature_of(u"1主页（HA010001）-1控制HiCam遥控器入口")
def before_feature_ControlEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@after_feature_of(u"1主页（HA010001）-1控制HiCam遥控器入口")
def after_feature_ControlEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"1主页（HA010001）-1控制HiCam遥控器入口")
def before_scenario_ControlEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@after_scenario_in_feature_of(u"1主页（HA010001）-1控制HiCam遥控器入口") 
def after_scenario_ControlEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    
