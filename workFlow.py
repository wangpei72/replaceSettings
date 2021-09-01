#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import targetFileStrReplacer as tfsr
import linesCommentMaker as lcm

hasDone = False
project_prefix = "/Users/wangpei/git-replace-test" # need
project_name = "AliSourcingImage" # need
target_b_g = "build.gradle"
target_g_w_p = "gradle/wrapper/gradle-wrapper.properties"
target_m_b_g= "Main/build.gradle"
target_g_p = "gradle.properties"
target_s_g = "settings.gradle"
target_m_g_p = "Main/gradle.properties"
target_l_p = "local.properties"


def gen_file_path(tar_f):
    file_path = get_file_path(project_name, tar_f, project_prefix)
    blue_print("generating file_path... res: %s" % file_path)
    return file_path


def get_file_path(project_name_, target_file, prefix="/Users/wangpei/git-groups"):
    file_path = os.path.join(prefix, project_name_, target_file)
    return file_path


def color_print(string):
    print("\033[1;31;40m %s\033[0m" % string)


def blue_print(string):
    print("\033[1;33;44m %s\033[0m" % string)


def replace_build_gradle(tar_f=target_b_g):
    print(" replacing build.gradle...")
    file_path = gen_file_path(tar_f)
    tfsr.replace_tar_str_allinone_print(file_path, "compileSdkVersion = 29", "compileSdkVersion = 30", True)
    tfsr.replace_tar_str_allinone_print(file_path, "targetSdkVersion = 29", "targetSdkVersion = 30", True)
    lines_content_list = []
    lines_src = lcm.get_file_path_lines(file_path)
    lines_content_list.append(lcm.find_content_str_line_num(lines_src, content_str="global_supportLibraryVersion='28.0.0'"))
    lines_content_list.append(lcm.find_content_str_line_num(lines_src, content_str="screenOrientation='unspecified'"))
    lcm.make_lines_comment(file_path, lines_content_list)


def replace_g_w_p(tar_f=target_g_w_p):
    print("replacing gradle-wrapper.properties...")
    file_path = gen_file_path(tar_f)
    tfsr.replace_tar_str_allinone_print(file_path, str_tar="distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip",
                                        str_replace="distributionUrl=https\://mtl-gradle-mirror.oss-cn-hangzhou.aliyuncs.com/gradle-6.6-all.zip",
                                        button=True)


def replace_s_g(tar_f=target_s_g):
    print("replacing settings.properties...")
    file_path = gen_file_path(tar_f)
    tfsr.replace_tar_str_allinone_print(file_path, str_tar="System.properties['androidGradlePluginVersion'] = \"4.0.1\"",
                                        str_replace="//  System.properties['androidGradlePluginVersion'] = \"4.1.0\"",
                                        button=True)


def replace_m_b_g(tar_f=target_m_b_g):
    print("replacing Main/build.gradle...")
    file_path = gen_file_path(tar_f)
    lines_src = lcm.get_file_path_lines(file_path)
    line_content_num = lcm.find_content_str_line_num(lines_src, content_str="manifestPlaceholders = [CHANNEL_VALUE: \"play\"," \
                                                                " SCREEN_ORIENTATION: rootProject.ext.screenOrientation]")
    lcm.make_line_comment(file_path, line_content_num)


def replace_g_p(tar_f=target_g_p):
    print("replacing gradle.properties...")
    file_path = gen_file_path(tar_f)
    # 该函数只能执行一次 不然会导致无限闭包，第二行不停的增加，这是由于利用替换取代增添代码的逻辑
    tfsr.replace_tar_str_allinone_print(file_path, str_tar="android.enableJetifier=true",
                                        str_replace="android.enableJetifier=true\n"
                                                    "dependency.locations.enabled=false",
                                        button=True)


def replace_m_b_g_no_deletion(tar_f=target_m_b_g):
    print("replacing Main/build.gradle without deletion...")
    file_path = gen_file_path(tar_f)
    tfsr.replace_tar_str_allinone_print(file_path, str_tar="htmlReport true",
                                        str_replace="htmlReport false",
                                        button=True)
    # lines_src = lcm.get_file_path_lines(file_path)
    # line_content_num = lcm.find_content_str_line_num(lines_src, content_str="preBuild.dependsOn projectReport")
    tfsr.replace_tar_str_allinone_print(file_path, str_tar="preBuild.dependsOn projectReport",
                                        str_replace="// preBuild.dependsOn projectReport\n"
                                                    "preBuild.dependsOn dependencyReport\n"
                                                    "preBuild.dependsOn propertyReport",
                                        button=True)


def start_work_flow():
    color_print("work flow start")
    replace_build_gradle()
    replace_g_w_p()
    replace_s_g()
    replace_m_b_g()
    replace_m_b_g_no_deletion()
    color_print("work flow done")


if __name__ == "__main__":
    has_args = True
    if len(sys.argv) != 3:
        has_args = False
        print("This .py is used for replacing settings content for a git repo when upgrading to target 30\n"
              "Usage : python workFlow.py [-p] [-n]\n"
              "-p: prefix path for a git repo, e.g.: /Users/xxx/git-groups\n"
              "-n: target git repository's name, e.g.: AliSourcingImage\n")
    if has_args:
        project_prefix = sys.argv[1]
        project_name = sys.argv[2]
        start_work_flow()
        if not hasDone:
            # replace_g_p()
            pass
        hasDone = True
