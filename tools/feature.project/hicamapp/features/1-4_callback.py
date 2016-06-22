# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d

@before_feature_of(u"1主页（HA010001）-4HiCam设置入口")
def before_feature_SettingsEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    

@after_feature_of(u"1主页（HA010001）-4HiCam设置入口")
def after_feature_SettingsEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"1主页（HA010001）-4HiCam设置入口")
def before_scenario_SettingsEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@after_scenario_in_feature_of(u"1主页（HA010001）-4HiCam设置入口") 
def after_scenario_SettingsEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    