# -*- coding: utf-8 -*- 
from lettuce import *
import time
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-3显示已经录制的时间")
def before_feature_GalleryEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        #open HicamAapp
        ex.start_activity("com.hicamapp/.activity.HomePage")
        connect.connect_hicam("HiCam38B78")
    except Exception as e:
        print e
    
@after_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-3显示已经录制的时间")
def after_feature_GalleryEnter(feature):
    try:
        connect.delete_img()
        d.press("back")  
        d.press("back")
        d.press("back")
        d.press("home")
    except Exception as e:
        print e
        

@before_scenario_in_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-3显示已经录制的时间")
def before_scenario_GalleryEnter(scenario):
    time.sleep(2)
    
    
@after_scenario_in_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-3显示已经录制的时间") 
def after_scenario_GalleryEnter(scenario):
    if d(resourceId="com.hicamapp:id/btn_operate_stop").exists:
        d(resourceId="com.hicamapp:id/btn_operate_stop").click.wait()
    if d(resourceId="com.hicamapp:id/grid_gallery").exists:
        d.press("back")
    d.press("back")

   
