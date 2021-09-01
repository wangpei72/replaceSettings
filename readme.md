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

## 脚本使用方式

```sh
chmod +x do_replace.sh
./do_replace.sh <prefix>
```

prefix: 指定的仓库前缀路径

## 使用案例

输入：

首先将需要升级参数的git-repos克隆至本地，并且统一放在一个父文件夹内，该父文件夹的目录作为prefix参数传递给脚本

```
./do_replace.sh /Users/wangpei/git-group-seller-project      
```

输出：

```sh
current path is /Users/wangpei/workspace/replaceSettings
job starting...
repo nums in total: 1
 now is doing job for biz_desktop... 
M       .gitignore
M       Main/build.gradle
M       build.gradle
M       gradle.properties
M       gradle/wrapper/gradle-wrapper.properties
M       settings.gradle
Branch 'feature/upgrade_target30' set up to track remote branch 'develop' from 'origin'.
Reset branch 'feature/upgrade_target30'
Your branch is up to date with 'origin/develop'.
prefix is /Users/wangpei/git-group-seller-project
target repo name is biz_desktop
 work flow start
replacing build.gradle...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/build.gradle
target str "compileSdkVersion = 29" not found
target str "targetSdkVersion = 29" not found
replacing gradle-wrapper.properties...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/gradle/wrapper/gradle-wrapper.properties
target str "distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip" not found
replacing settings.properties...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/settings.gradle
target str "System.properties['androidGradlePluginVersion'] = "4.0.1"" not found
replacing Main/build.gradle...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/Main/build.gradle
replacing Main/build.gradle without deletion...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/Main/build.gradle
target str "htmlReport true" not found
target str "preBuild.dependsOn projectReport" not found
 work flow done
replacing gradle.properties...
 generating file_path... res: /Users/wangpei/git-group-seller-project/biz_desktop/gradle.properties
 /Users/wangpei/git-group-seller-project/biz_desktop/gradle.properties has done for replacing, aborting...
[feature/upgrade_target30 a66173b] feature:执行do_replace.sh脚本,替换构建参数文本
 6 files changed, 22 insertions(+), 10 deletions(-)
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 12 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (11/11), 1.16 KiB | 1.16 MiB/s, done.
Total 11 (delta 8), reused 0 (delta 0), pack-reused 0
To gitlab.alibaba-inc.com:ANDROID_SELLER_JDY_MODULES/biz_desktop.git
   a91473d..a66173b  feature/upgrade_target30 -> feature/upgrade_target30
 done job for biz_desktop... 
 job done. 
```

有关文本替换的log信息可以在：父目录/write.logs日志文件中获取

## 其他说明

do_replace.sh中指明了当前需要做文本替换的仓库名称，变量repo_name_list是一个字符串列表，用来指定所有的仓库名称列表

```
repo_name_list=(
  biz_desktop
  # 请在这里添加你需要的仓库名称
)
```

## 一些资源

- 卖家在役仓库的名称list，主工程AlibabaSupplier已经被排除在外

```
  AlibabaSupplierMember 
  AliSupplierHermes 
  CloudMeeting_Android 
  AlibabaSupplierKit 
  AliSupplierAlivePush 
  AlibabaSupplierPoplayer 
  biz_mc 
  AliSupplierBizBase 
  AlibabaSupplierBizSearch 
  AliSupplierImage 
  AliSupplierCorePlugin 
  AliSupplierBoot 
  AliSourcingSubtitle 
  AliSupplierLanguage 
  ICBU_Flutter_DPL 
  biz_tango 
  openIMKitUtility 
  SteelORM 
  KeyTool 
  FileSelector_Android 
  Alibaba-Android-CI 
  jdy_android 
  ASTangoModule 
  QianniuAnnotationProcessor 
  QianniuAnnotation
  biz_desktop
```

- 买家仓库的名称list，主工程排除在外

```
 PackageGatekeeper  
  mtl-gradle-plugin-lite  
  testcomparator  
  AliSourcingVideoTalk  
  StripR  
  facebook-android-sdk  
  AliOneTouchPartnerProject  
  AliSourcingPDK  
  buildscript  
  AliSourcingBase  
  AliSourcingLinkInSDK
```

