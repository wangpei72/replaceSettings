这是一个用来对一个sdk模块仓库中类似build.gradle Main/build.gradle gradle.properties
等文件中，为了升级到target30而需要更改的参数进行自动化文本替换的脚本仓库

包括了具有以下功能的脚本：
- 获取一个项目组下所有项目的文件清单，存在./fileLists*文件夹中
- 将文件中某一行或者多行文本注释
- 找到具体文本内容所在行
- 将指定文件中某一文本内容替换成指定的其他文本内容
- 根据target30升级中需要配置的参数变更项自动化应用到任意项目组任意目标仓库

如果需要扩展变更项条目，请在workflow.py中扩展