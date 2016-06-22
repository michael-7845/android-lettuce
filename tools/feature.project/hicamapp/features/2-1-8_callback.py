# -*- coding: utf-8 -*- 
from lettuce import *
import time
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-8录像")
def before_feature_GalleryEnter(feature):
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

@after_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-8录像")
def after_feature_GalleryEnter(feature):
    
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-8录像")
def before_scenario_GalleryEnter(scenario):
    pass

@after_scenario_in_feature_of(u"2取景模式（HA0101)-1普通录像(HA010101)-8录像") 
def after_scenario_GalleryEnter(scenario):
    if d(text="I Know").exists:
        
        ex.start_activity("com.android.settings/.Settings")
        print "open settings"
        d(text="WLAN").click.wait()
        if d(resourceId="com.mediatek:id/imageswitch",checked=False).exists:
            
            d(resourceId="com.mediatek:id/imageswitch").click.wait()
            print "open wifi"
        d.press("back")
        d.press("back")
        d(text="I Know").click.wait()
        d.press("back")
        d.press("back")
        d.press("back")
        d.press("back")
        try:
            #open HicamAapp
            ex.start_activity("com.hicamapp/.activity.HomePage")
            #connect device
            connect.connect_hicam("HiCam38B78")
            d(className="android.widget.LinearLayout",index=0).child(className="android.widget.ImageButton",index=0).click.wait()
            time.sleep(2)
            if d(resourceId="com.hicamapp:id/text_record_duration").exists:
                time.sleep(2)
                d(resourceId="com.hicamapp:id/btn_operate_stop").click.wait()
        except Exception as e:
            print e
    d.press("back")
    time.sleep(2)
   