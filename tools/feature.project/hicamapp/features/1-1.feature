language: zh-CN
特性: 1主页（HA010001）-1控制HiCam遥控器入口
 
    @F1
    场景: 1有网络
        1、打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、设备连接自动弹出: 在【5000】毫秒内，文本【"Connection:"】应该出现
        3、选择wifi连接:点击页面元素【resourceId=com.hicamapp:id/text_wifi】
        4、在wifi列表中选择摄像头热点:手指纵向滚动框架【resourceId=com.hicamapp:id/list】至页面元素【text=HiCamC5DDF】
        5、选择HiCam98EE6热点:点击页面元素【text=HiCamC5DDF】
        6、点击设备的名称:点击页面元素，父【resourceId=com.hicamapp:id/list】自【className=android.widget.RelativeLayout,index=0】
        7、连接成功，选择框消失:在【5000】毫秒内，文本【"Devices"】应该消失
        
        8、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        9、下方3个按键: 页面元素【className=android.widget.Button】的数量应该为【3】
        10、点击主界面按钮: 点击页面元素【className=android.widget.ImageButton,index=0】
        11、验证主界面Controller文字: 应该可看到文本【"Controller"】
        12、验证主界面Editor文字: 应该可看到文本【"Editor"】
        13、验证主界面Watch文字: 应该可看到文本【"Watch"】
        
    @F1
    场景: 2无网络
        1、打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、设备连接自动弹出: 在【5000】毫秒内，文本【"Connection:"】应该出现
        3、取消连接窗口:点击文本【"Cancel"】
        4、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        5、验证未进入控制器:应该看不到页面元素【resourceId=com.hicamapp:id/btn_settings】
