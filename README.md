# nuke-project-default-setting


nuke默认参数设置

用于改变nuke默认的工程大小，帧速率以及一些其他常用节点默认参数

用法：把menu.py和Set_project.py下载放到.nuke文件夹，如果文件夹已存在menu.py文件，就把下载的menu.py文件里的代码复制粘贴到已存在的menu.py

启动NUKE后在菜单栏最后找到Set the project default选项打开

界面参数：

width-----------------------------------------------------工程默认宽度 

height----------------------------------------------------工程默认高度 

pixel aspect----------------------------------------------工程默认像素宽高比 

fps-------------------------------------------------------工程默认帧速率

write default channels------------------------------------Write节点默认输出通道

write mov default encoding--------------------------------Write节点输出mov文件时默认编码

write mov automatically check "write time code"-----------如果选中，Write节点输出mov文件时会自动勾选write time code选项

viewer automatically check "full_frame_processing"--------如果选中，预览窗口会自动勾选full_frame_processing，每次预览都会渲染全画幅

read raw data---------------------------------------------如果选中，Read节点自动勾选raw data

write raw data--------------------------------------------如果选中，Write节点自动勾选raw data

retime automatically output to the project start frame----如果选中，创建的Retime节点会自动偏到工程设置的起始帧

rendering automatically create a rendering path-----------如果选中，Write节点在渲染时会判断渲染路径是否存在，若不存在会自动创建路径，防止渲染路径不存在出现渲染错误



注意所有功能在设置完后要重启一次NUKE才能生效



