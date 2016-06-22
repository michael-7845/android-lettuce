# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d
import connect

@before_feature_of(u"11连接-1下载分类")
def before_feature_SettingsEnter(feature):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    ''''try:
        #open HicamAapp
        ex.start_activity("com.hicamapp/.activity.HomePage")
        #connect device
        connect.connect_hicam("HiCam38B78")
        #connect.connect_hicam("HiCamB8271")
    except Exception as e:
        print e
    '''
@after_feature_of(u"11连接-1下载分类")
def after_feature_SettingsEnter(feature):
    connect.delete_img()
    ex.delete_allfiles_under("/sdcard/HiCamApp")
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")

@before_scenario_in_feature_of(u"11连接-1下载分类")
def before_scenario_SettingsEnter(scenario):
    d.press("back")  
    d.press("back")
    d.press("back")
    d.press("home")
    try:
        #open HicamAapp
        ex.start_activity("com.hicamapp/.activity.HomePage")
        
        #connect device
        connect.connect_hicam("HiCam38B78")
        #connect.connect_hicam("HiCamB8271")
    except Exception as e:
        print e

@after_scenario_in_feature_of(u"11连接-1下载分类") 
def after_scenario_SettingsEnter(scenario):
    d.press("back")  
    d.press("back")  
    d.press("back")  
    d.press("back")  
    d.press("home")  
    # if d(text="Complete").exists:
        # d.press("back")  
    # if d(resourceId="com.hicamapp:id/container_title_media_detail").exists:
        # d.press("back")
    # if d(resourceId="com.hicamapp:id/container_media_thumb_title").exists:
        # d.press("back")
    # if d(resourceId="com.hicamapp:id/btn_operate_start").exists:
        # d.press("back")

    