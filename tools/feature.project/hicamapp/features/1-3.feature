language: zh-CN
特性: 1主页（HA010001）-3HiCam相册入口

    @F1
    场景: 1有网络
        1、打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、设备连接自动弹出: 在【5000】毫秒内，文本【"Connection:"】应该出现
        3、选择wifi连接:点击页面元素【resourceId=com.hicamapp:id/text_wifi】
        4、在wifi列表中选择摄像头热点:手指纵向滚动框架【resourceId=com.hicamapp:id/list】至页面元素【text=HiCamC5DDF】
        5、选择HiCamC5DDF热点:点击页面元素【text=HiCamC5DDF】
        6、点击设备的名称:点击页面元素，父【resourceId=com.hicamapp:id/list】自【className=android.widget.RelativeLayout,index=0】
        7、连接成功，选择框消失:在【5000】毫秒内，文本【"Devices"】应该消失
        
        8、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        9、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        10、检查相册中的关键UI:应该可看到页面元素【resourceId=com.hicamapp:id/container_gallery_back】
        11、back两次返回至Home界面:点按物理键【back】【2】次
        12、验证主界面Controller文字: 应该可看到文本【"Controller"】
        13、验证主界面Editor文字: 应该可看到文本【"Editor"】
        14、验证主界面Watch文字: 应该可看到文本【"Watch"】
    
    @F1
    场景: 2无网络
        1、打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、设备连接自动弹出: 在【5000】毫秒内，文本【"Connection:"】应该出现
        3、取消连接窗口:点击文本【"Cancel"】
        4、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        5、验证无法进入控制器查看不了相册:应该看不到页面元素【resourceId=com.hicamapp:id/btn_settings】
    