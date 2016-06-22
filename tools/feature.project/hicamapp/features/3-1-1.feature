language: zh-CN
特性: 3相册（HA0102)-1读取照片(HA010201)-1读取照片信息，显示拍照时间

    @F1
    场景: 1无地理位置照片信息获取
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Photo选项:点击页面坐标【904,1380】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待刷新图标消失:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、检查图片预览界面:应该看不到页面元素【resourceId=com.hicamapp:id/location】

    @F1
    场景: 3基本信息
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Photo选项:点击页面坐标【904,1380】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待刷新图标消失:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、检查缩略图信息:应该可看到页面元素【resourceId=com.hicamapp:id/text_picture_date】
        
    @F1
    场景: 4显示拍照时间
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Photo选项:点击页面坐标【904,1380】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待刷新图标消失:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、检查缩略图信息:应该可看到页面元素【resourceId=com.hicamapp:id/text_picture_date】
    
    @F1
    场景: 5单击照片
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、打开模式切换:点击页面元素【resourceId=com.hicamapp:id/btn_mode】
        3、选择Photo选项:点击页面坐标【904,1380】
        4、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        5、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        6、等待刷新图标消失:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        7、打开第一张图片:点击页面元素，父【resourceId=com.hicamapp:id/grid_gallery】自【className=android.widget.RelativeLayout,index=0】
        8、验证进入大图查看:应该可看到页面元素【resourceId=com.hicamapp:id/container_title_media_detail】