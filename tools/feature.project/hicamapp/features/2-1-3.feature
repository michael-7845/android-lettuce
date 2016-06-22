language: zh-CN
特性: 2取景模式（HA0101)-1普通录像(HA010101)-3显示已经录制的时间
    
    @F1 
    场景: 2录制中显示变化
        1、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择普通录像选项:点击页面坐标【904,680】
        4、录像开始:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、录制5秒:等待【5000】毫秒，不做任何操作
        6、观察时间变化:应该看不到文本【"00:00:00"】
        7、观察时间变化:在【5000】毫秒内，文本【"00:00:09"】应该出现


    @F1 @test2
    场景: 3录制后时间显示
        1、进入HiCam控制器:点击页面元素，父【className=android.widget.LinearLayout,index=0】自【className=android.widget.ImageButton,index=0】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择普通录像选项:点击页面坐标【904,680】
        4、录像开始:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、录制5秒:等待【5000】毫秒，不做任何操作
        6、录像结束:点击页面元素【resourceId=com.hicamapp:id/btn_operate_stop】
        7、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        8、检查录制后的时间显示:应该可以看见页面元素父【className=android.widget.RelativeLayout,index=0】子【className=android.widget.RelativeLayout,index=1】自【className=android.widget.RelativeLayout,index=0】的文本为【"00:00:04"】