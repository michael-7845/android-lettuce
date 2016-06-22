# -*- coding: utf-8 -*- 
from lettuce import *
import uiautomator.uiautomatorEx as ex
from uiautomator.myDevice import device as d

def connect_hicam(DeviceName):
    try:
        #temp
        DeviceName = "HiCamC5DDF"
        if d(resourceId="com.hicamapp:id/bt_change").exists:
            d(resourceId="com.hicamapp:id/bt_change").click.wait()
        #connect hicam
        d(resourceId="com.hicamapp:id/text_wifi").click.wait()
        d(resourceId="com.hicamapp:id/list").scroll.vert.to(text=DeviceName)
        d(text="Devices").wait.exists(timeout=5000)
        d(text=DeviceName).click.wait()
        d(resourceId="com.hicamapp:id/list").child(className="android.widget.RelativeLayout",index=0).click.wait()
        d(text="Devices").wait.gone(timeout=5000) 
    except Exception as e:
        print e
        
def delete_img():
    try:
        d(resourceId="com.hicamapp:id/bt_controllet").click.wait()
        d(resourceId="com.hicamapp:id/btn_media").click.wait()
        d(className="android.widget.RelativeLayout",index=0).child(resourceId="com.hicamapp:id/img_thumb",index=0).long_click()
        d(resourceId="com.hicamapp:id/text_media_select_all").click.wait()
        d(resourceId="com.hicamapp:id/btn_media_delete").click.wait()
        #confir button:d(text="OK").click.wait()
        d.click(540, 1684)
        d.wait.update()
    except Exception as e:
        print e
    
def take_picture(times):
    try:
        #enter controller
        d(resourceId="com.hicamapp:id/bt_controllet").click.wait()
        #create test picture
        d(resourceId="com.hicamapp:id/btn_mode").click.wait()
        d.click(904,1380)
        d.wait.update()
        i = 0
        while i < times:
            d(resourceId="resourceId=com.hicamapp:id/btn_operate_start").click.wait()
            i += 1
    except Exception as e:
        print e
        
def click_ok_btn():
    #confir button:d(text="OK").click.wait()
    d.click(540, 1684)
    d.wait.update()
    
# def connect_wifi():
    # '''
    # 1、启动活动【com.android.settings/.Settings】
    # 2、点击文本【"WLAN"】
    # 3、点击页面元素【text=关闭】
    # 4、在【5000】毫秒内，文本【"要查看可用网络，请打开 WLAN。"】应该消失
    # 5、手指纵向滚动框架【className=android.widget.ListView】至文本【"CK-Test-VAS2"】
    # 6、点击文本【"CK-Test-VAS2"】
    # 7、在页面元素【className=android.widget.EditText】添加文本【"test963852741"】
    # 8、点击文本【"连接"】
    # 9、手指向下边结束位置滚动框架【className=android.widget.ListView】
    # 10、在【20000】毫秒内，文本【"已连接"】应该出现
    # '''
    
    # ex.start_activity("com.android.settings/.Settings")
    # d(text="WLAN").click.wait()
    # d(text="关闭").click.wait()
    # assert d(text="要查看可用网络，请打开 WLAN。").wait.gone(timeout=5000)
    # d(className="android.widget.ListView").scroll.vert.to(text="CK-Test-VAS2")
    # d(text="CK-Test-VAS2").click.wait()
    # d(className="android.widget.EditText").set_text("test963852741")
    # d.wait.idle()
    # d(text="连接").click.wait()
    # d(className="android.widget.ListView").scroll.vert.toBeginning()
    # d.wait.idle()
    # assert d(text="已连接").wait.exists(timeout=20000)
    
    # d.press("back")  
    # d.press("back")
    # d.press("back")
    # d.press("home")
    
# def disconnect_wifi(feature):
    # '''
    # 1、启动活动【com.android.settings/.Settings】
    # 2、点击文本【"WLAN"】
    # 3、长按页面元素【text=已连接】
    # 4、点击文本【"取消保存网络"】
    # 5、点击文本【"打开"】
    # '''
    
    # ex.start_activity("com.android.settings/.Settings")
    # d(text="WLAN").click.wait()
    # d(text="已连接").long_click()
    # d.wait.update()
    # d(text="取消保存网络").click.wait()
    # d(text="打开").click.wait()
    
    # d.press("back")  
    # d.press("back")
    # d.press("back")
    # d.press("home")