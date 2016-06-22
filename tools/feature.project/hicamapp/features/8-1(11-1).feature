language: zh-CN
特性: 11连接-1下载分类
    XS坐标:
    video:【904,680】
    Photo:【904,1380】
    Burst:【904,1550】
    Lapse:【904,1016】
    Slow:【904,1200】
    
    @F1
    场景: 1普通照片
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择普通照相选项:点击页面坐标【904,1380】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        8、设置初始文件数检查点:设置路径【/sdcard/HiCamApp】下【jpg】类型文件数检查点
        9、点击下载按钮:点击页面元素【resourceId=com.hicamapp:id/btn_media_save】
        10、等待下载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/text_media_download_status,text=Complete】应该出现
        11、文件应该增加1个:路径【/sdcard/HiCamApp】下【jpg】类型文件数相对上个检查点应该增加【1】

    @F1
    场景: 2连续照片
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择连续拍照选项:点击页面坐标【904,1550】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        8、设置初始文件数检查点:设置路径【/sdcard/HiCamApp】下【jpg】类型文件数检查点
        9、点击下载按钮:点击页面元素【resourceId=com.hicamapp:id/btn_media_save】
        10、等待下载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/text_media_download_status,text=Complete】应该出现
        11、文件应该增加1:路径【/sdcard/HiCamApp】下【jpg】类型文件数相对上个检查点应该增加【1】
        
    @F1 @debug
    场景: 3普通录像
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择普通录像选项:点击页面坐标【904,680】
        4、录像开始:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、录制5秒:等待【5000】毫秒，不做任何操作
        6、录像结束:点击页面元素【resourceId=com.hicamapp:id/btn_operate_stop】
        7、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        8、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        9、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        10、设置初始文件数检查点:设置路径【/sdcard/HiCamApp】下【3gp】类型文件数检查点
        11、点击下载按钮:点击页面元素【resourceId=com.hicamapp:id/btn_media_save】
        12、等待下载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/text_media_download_status,text=Complete】应该出现
        13、文件应该增加1:路径【/sdcard/HiCamApp】下【3gp】类型文件数相对上个检查点应该增加【1】
        
    @F1 @debug
    场景: 4延时录像
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择延时录像选项:点击页面坐标【904,1016】
        4、录像开始:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、录制5秒:等待【5000】毫秒，不做任何操作
        6、录像结束:点击页面元素【resourceId=com.hicamapp:id/btn_operate_stop】
        7、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        8、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        9、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        10、设置初始文件数检查点:设置路径【/sdcard/HiCamApp】下【3gp】类型文件数检查点
        11、点击下载按钮:点击页面元素【resourceId=com.hicamapp:id/btn_media_save】
        12、等待下载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/text_media_download_status,text=Complete】应该出现
        13、文件应该增加1:路径【/sdcard/HiCamApp】下【3gp】类型文件数相对上个检查点应该增加【1】
        
    @F1 @debug
    场景: 5高速录像
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择高速录像选项:点击页面坐标【904,1200】
        4、录像开始:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、录制5秒:等待【5000】毫秒，不做任何操作
        6、录像结束:点击页面元素【resourceId=com.hicamapp:id/btn_operate_stop】
        7、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        8、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        9、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        10、设置初始文件数检查点:设置路径【/sdcard/HiCamApp】下【3gp】类型文件数检查点
        11、点击下载按钮:点击页面元素【resourceId=com.hicamapp:id/btn_media_save】
        12、等待下载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/text_media_download_status,text=Complete】应该出现
        13、文件应该增加1:路径【/sdcard/HiCamApp】下【3gp】类型文件数相对上个检查点应该增加【1】