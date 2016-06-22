# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"1主页（HA010001）-3HiCam相册入口")
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

def connect_hicam(DeviceName):
    #connect hicam
    d(resourceId="com.hicamapp:id/text_wifi").click.wait()
    d(resourceId="com.hicamapp:id/list").scroll.vert.to(text=DeviceName)
    d(text="Devices").wait.exists(timeout=5000)
    d(text=DeviceName).click.wait()
    d(resourceId="com.hicamapp:id/list").child(className="android.widget.RelativeLayout",index=0).click.wait()
    d(text="Devices").wait.gone(timeout=5000)  
    
    
@after_feature_of(u"1主页（HA010001）-3HiCam相册入口")
def after_feature_GalleryEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"1主页（HA010001）-3HiCam相册入口")
def before_scenario_GalleryEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@after_scenario_in_feature_of(u"1主页（HA010001）-3HiCam相册入口") 
def after_scenario_GalleryEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

   
