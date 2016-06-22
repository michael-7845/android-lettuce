# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"7收看视频直播（HA0106)-1看直播界面（HA010601）-1")
def before_feature_SettingsEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        #open HicamAapp
        ex.start_activity("com.hicamapp/.activity.HomePage")
        #connect device
        connect.connect_hicam("HiCam38B78")
    except Exception as e:
        print e

@after_feature_of(u"7收看视频直播（HA0106)-1看直播界面（HA010601）-1")
def after_feature_SettingsEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"7收看视频直播（HA0106)-1看直播界面（HA010601）-1")
def before_scenario_SettingsEnter(scenario):
    pass

@after_scenario_in_feature_of(u"7收看视频直播（HA0106)-1看直播界面（HA010601）-1") 
def after_scenario_SettingsEnter(scenario):
    d.press("back")  
    