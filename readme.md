# 【升级Target 30】文本替换脚本使用说明

这是一个用来对一个sdk模块仓库中类似build.gradle Main/build.gradle gradle.properties
等文件中，为了升级到target30而需要更改的参数进行自动化文本替换的脚本仓库

包括了具有以下功能的脚本：
- 获取一个项目组下所有项目的文件清单，存在./fileLists*文件夹中
- 将文件中某一行或者多行文本注释
- 找到具体文本内容所在行
- 将指定文件中某一文本内容替换成指定的其他文本内容
- 根据target30升级中需要配置的参数变更项自动化应用到任意项目组任意目标仓库

如果需要扩展变更项条目，请在workflow.py中扩展

## 当前脚本使用方式

```sh
chmod +x workFlow.py
./workFlow.py -p <prefix> -n <repo-name>
```

prefix: 指定的仓库前缀路径

repo-name：指定仓库名

## 使用该命令获取帮助

```sh
./workFlow.py -h
```



## 使用案例

输入：

```
 ./workFlow.py -p /Users/wangpei/git-replace-test -n AliSourcingImage
```

输出：

```sh
prefix is /Users/wangpei/git-replace-test
target repo name is AliSourcingImage
 work flow start
 replacing build.gradle...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/build.gradle
target str "compileSdkVersion = 29" not found
target str "targetSdkVersion = 29" not found
replacing gradle-wrapper.properties...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/gradle/wrapper/gradle-wrapper.properties
target str "distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip" not found
replacing settings.properties...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/settings.gradle
target str "System.properties['androidGradlePluginVersion'] = "4.0.1"" not found
replacing Main/build.gradle...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/Main/build.gradle
replacing Main/build.gradle without deletion...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/Main/build.gradle
target str "htmlReport true" not found
target str "preBuild.dependsOn projectReport" not found
 work flow done
replacing gradle.properties...
 generating file_path... res: /Users/wangpei/git-replace-test/AliSourcingImage/gradle.properties
 pkg-name/gradle.properties has done for replacing, aborting...
```

