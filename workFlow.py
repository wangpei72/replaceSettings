#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import time
import getopt
import targetFileStrReplacer as tfsr
import linesCommentMaker as lcm


button_ctl = True
hasDone = False
project_prefix = "/Users/wangpei/git-replace-test"  # need
project_name = "AliSourcingImage"  # need
target_b_g = "build.gradle"
target_g_w_p = "gradle/wrapper/gradle-wrapper.properties"
target_m_b_g = "Main/build.gradle"
target_g_p = "gradle.properties"
target_s_g = "settings.gradle"
target_m_g_p = "Main/gradle.properties"
target_l_p = "local.properties"


def gen_file_path(tar_f):
    file_path = get_file_path(project_name, tar_f, project_prefix)
    if button_ctl:
        color_print("generating file_path... res: %s" % file_path)
    return file_path


def get_file_path(project_name_, target_file, prefix="/Users/wangpei/git-groups"):
    file_path = os.path.join(prefix, project_name_, target_file)
    return file_path


def color_print(string):
    print("\033[1;31;40m %s\033[0m" % string)


def blue_print(string):
    print("\033[1;33;44m %s\033[0m" % string)


def replace_build_gradle(tar_f=target_b_g):
    log_print("replacing build.gradle...")
    file_path = gen_file_path(tar_f)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, "compileSdkVersion = 29", "compileSdkVersion = 30", button_ctl)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, "targetSdkVersion = 29", "targetSdkVersion = 30", button_ctl)
    lines_content_list = []
    lines_src = lcm.get_file_path_lines(file_path)
    lines_content_list.append(lcm.find_content_str_line_num(lines_src, content_str="global_supportLibraryVersion='28.0.0'"))
    lines_content_list.append(lcm.find_content_str_line_num(lines_src, content_str="screenOrientation='unspecified'"))
    lcm.make_lines_comment(file_path, lines_content_list)


def replace_g_w_p(tar_f=target_g_w_p):
    log_print("replacing gradle-wrapper.properties...")
    file_path = gen_file_path(tar_f)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, str_tar="distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip",
                                                 str_replace="distributionUrl=https\://mtl-gradle-mirror.oss-cn-hangzhou.aliyuncs.com/gradle-6.6-all.zip",
                                                 button=True)


def replace_s_g(tar_f=target_s_g):
    log_print("replacing settings.properties...")
    file_path = gen_file_path(tar_f)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, str_tar="System.properties['androidGradlePluginVersion'] = \"4.0.1\"",
                                                 str_replace="System.properties['androidGradlePluginVersion'] = \"4.1.0\"",  # ??????AGP???????????????????????????????????????
                                                 button=button_ctl)


def replace_m_b_g(tar_f=target_m_b_g):
    log_print("replacing Main/build.gradle...")
    file_path = gen_file_path(tar_f)
    lines_src = lcm.get_file_path_lines(file_path)
    line_content_num = lcm.find_content_str_line_num(lines_src, content_str="manifestPlaceholders = [CHANNEL_VALUE: \"play\"," \
                                                                " SCREEN_ORIENTATION: rootProject.ext.screenOrientation]")
    lcm.make_line_comment(file_path, line_content_num)


def replace_g_p(tar_f=target_g_p, monitor_path=os.path.join(project_prefix, "do-not-delete.txt")):
    log_print("replacing gradle.properties...")
    file_path = gen_file_path(tar_f)
    if not os.path.exists(monitor_path):
        print("monitor txt not exists")
        os.system(r"touch {}".format(monitor_path))
    lines_src = lcm.get_file_path_lines(monitor_path)
    line_content_num = lcm.find_content_str_line_num(lines_src, file_path)
    if line_content_num == -1:  # ??????????????????????????????
        # ??????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????????????????????
        log_print("into record and replacing gradle.properties...")
        record_first_for_do_job(file_path, monitor_path)
        tfsr.remark_n_replace_tar_str_allinone_print(file_path, str_tar="android.enableJetifier=true",
                                                     str_replace="android.enableJetifier=true\n"
                                                        "dependency.locations.enabled=false",
                                                     button=button_ctl)
        record_has_done_gp_for_this_path(file_path, monitor_path)
    else:
        blue_print("%s has done for replacing, aborting..." % file_path)
        logging.debug(file_path + " has done for replacing, aborting...")
        return


def record_has_done_gp_for_this_path(file_path, monitor_path):
    # with open(monitor_path, "a+") as fw:
    tfsr.replace_tar_str_allinone_print(monitor_path, file_path + " hasDone:False", file_path + " hasDone:True", button=button_ctl)


def record_first_for_do_job(file_path, monitor_path):
    with open(monitor_path, "a+") as fw:
        fw.write(file_path+" hasDone:False")


def replace_m_b_g_no_deletion(tar_f=target_m_b_g):
    log_print("replacing Main/build.gradle without deletion...")
    file_path = gen_file_path(tar_f)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, str_tar="htmlReport true",
                                                 str_replace="htmlReport false",
                                                 button=button_ctl)
    tfsr.remark_n_replace_tar_str_allinone_print(file_path, str_tar="preBuild.dependsOn projectReport",
                                                 str_replace="// preBuild.dependsOn projectReport\n"
                                                    "preBuild.dependsOn dependencyReport\n"
                                                    "preBuild.dependsOn propertyReport",
                                                 button=button_ctl)


def start_work_flow():
    color_print("work flow start")
    logging.debug("work flow start")
    replace_build_gradle()
    replace_g_w_p()
    replace_s_g()
    replace_m_b_g()
    replace_m_b_g_no_deletion()
    color_print("work flow done")
    logging.debug("work flow done")


def print_help():
    print("This .py is used for replacing settings content for a git repo when upgrading to target 30\n"
          "Usage : python workFlow.py -p <prefix-path> -n <repo-name>\n"
          "-p: prefix path for a git repo, e.g.: /Users/xxx/git-groups\n"
          "-n: target git repository's name, e.g.: AliSourcingImage\n")


def log_print(string):
    logging.debug(string)
    print(string)


if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:n:", ["pre=", "name="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-p", "--pre"):
            project_prefix = arg
        elif opt in ("-n", "--name"):
            project_name = arg
    logging.basicConfig(filename=os.path.join(project_prefix, "write.logs"), format='%(levelname)s:%(filename)s:%(asctime)s:%(message)s', level=logging.DEBUG)
    log_print("prefix is " + project_prefix)
    log_print("target repo name is " + project_name)
    start_work_flow()
    replace_g_p(monitor_path=os.path.join(project_prefix, "do-not-delete.txt"))
    logging.debug("\n\n")
