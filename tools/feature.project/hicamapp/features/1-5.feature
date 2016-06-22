language: zh-CN
特性: 1主页（HA010001）-5设备发现 

    @F1 @1st_enter
    场景: 1第一次进入APP
        1、打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、弹出连接窗口:在【5000】毫秒内，文本【"Connection:"】应该出现
        3、点击cancel:点击文本【"Cancel"】
        4、退出app:点按物理键【back】【2】次
        5、验证是否退出App:应该看不到页面元素【resourceId=com.hicamapp:id/bt_change】
    
    @F1
    场景: 2搜索到设备
        1、进入APP:打开HiCamApp: 启动活动【com.hicamapp/.activity.HomePage】
        2、弹出连接窗口:在【5000】毫秒内，文本【"Connection:"】应该出现
        3、选择wifi连接:点击页面元素【resourceId=com.hicamapp:id/text_wifi】
        4、显示搜索到的WiFi热点:在【5000】毫秒内，页面元素【resourceId=com.hicamapp:id/name】应该出现
        5、点击cancel:点击文本【"Cancel"】
        6、退出app:点按物理键【back】【2】次
        7、应该看不到页面元素【resourceId=com.hicamapp:id/bt_change】

