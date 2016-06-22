language: zh-CN
特性: 7收看视频直播（HA0106)-1看直播界面（HA010601）-1

    @F1
    场景: 1点击播放
        1、打开watch:点击页面元素【resourceId=com.hicamapp:id/btn_live】
        2、选择近场wifi:点击文本【"Here"】
        3、验证是否播放成功:应该可看到页面元素【resourceId=com.hicamapp:id/tv_time】
    
    @F1
    场景: 3返回Home界面
        1、打开watch:点击页面元素【resourceId=com.hicamapp:id/btn_live】
        2、选择近场wifi:点击文本【"Here"】
        3、播放中按返回键:点按物理键【back】
        4、验证主界面Controller文字: 应该可看到文本【"Controller"】
        5、验证主界面Editor文字: 应该可看到文本【"Editor"】
        6、验证主界面Watch文字: 应该可看到文本【"Watch"】