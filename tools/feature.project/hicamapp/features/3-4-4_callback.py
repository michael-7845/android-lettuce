# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"3相册（HA0102)-4图片查看界面-4图片查看界面")
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

@after_feature_of(u"3相册（HA0102)-4图片查看界面-4图片查看界面")
def after_feature_SettingsEnter(feature):
    connect.delete_img()
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"3相册（HA0102)-4图片查看界面-4图片查看界面")
def before_scenario_SettingsEnter(scenario):
    pass

@after_scenario_in_feature_of(u"3相册（HA0102)-4图片查看界面-4图片查看界面") 
def after_scenario_SettingsEnter(scenario):
    d.press("back")  
    d.press("back")
    