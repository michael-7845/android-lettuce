language: zh-CN
特性: 3相册（HA0102)-4图片查看界面-4图片查看界面

    @F1
    场景: 4无图片
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        3、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        4、检查图片预览界面:应该看不到页面元素【resourceId=com.hicamapp:id/grid_gallery】

    @F1
    场景: 6缩略图
        1、进入控制器:点击页面元素【resourceId=com.hicamapp:id/bt_controllet】
        2、拍照:点击页面元素【resourceId=com.hicamapp:id/btn_operate_start】
        3、进入相册:点击页面元素【resourceId=com.hicamapp:id/btn_media】
        4、等待加载完成:在【60000】毫秒内，页面元素【resourceId=com.hicamapp:id/container_gallery_back】应该出现
        5、等待3秒:等待【3000】毫秒，不做任何操作
        6、检查缩略图:应该可看到页面元素【resourceId=com.hicamapp:id/text_picture_date】
        7、检查图片类型图标:应该可看到页面元素【resourceId=com.hicamapp:id/img_picture_type】
