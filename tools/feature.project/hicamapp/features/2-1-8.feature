language: zh-CN
特性: 2取景模式（HA0101)-1普通录像(HA010101)-8录像
    
    @F1 
    场景: 1录像界面
        1、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Video选项:点击页面坐标【904,680】
        4、检查录像界面:应该可看到页面元素【resourceId=com.hicamapp:id/btn_mode,text=VIDEO】

    @F1
    场景: 2录像中断开连接
        1、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        2、设置为录像模式:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Video选项:点击页面坐标【904,680】
        4、检查录像界面:应该可看到页面元素【resourceId=com.hicamapp:id/btn_mode,text=VIDEO】
        5、录制一个视频:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        6、打开系统设置:启动活动【com.android.settings/.Settings】
        7、进入WLAN:点击文本【"WLAN"】
        8、关闭wifi:点击页面元素【resourceId=com.mediatek:id/imageswitch】
        9、退出设置:点按物理键【back】【2】次
        10、检查App状态:在【10000】毫秒内，文本【"Connection fail,please check your network and try again"】应该出现