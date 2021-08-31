#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re


def get_java_file_list_from_root(filepath, suffix="", file_lists_dir="fileListsTest"):
    # 遍历filepath下所有java文件，包括子目录
    files = os.listdir(filepath)
    reg = re.compile(r"\..*")
    regForJava = re.compile(r"\.java")
    regForXml = re.compile(r"\.xml")
    regForSettings = re.compile(r"\.properties|\.gradle")
    regForPro = re.compile(r"\.pro$")
    regForOthers = re.compile(r"\.sh|\.xml|\.bat|\.jar|\.MD|\.md|\.png|\.txt|\.json|\.flat|\.class|\.gif|\.so"
                              r"|\.py|gradlew")

    curDiry = os.path.dirname(os.path.realpath(__file__))
    for fi in files:
        if reg.match(fi) is not None or regForXml.search(fi) is not None or regForJava.search(fi) is not None or regForOthers.search(fi) is not None or regForPro.search(fi) is not None:
            continue
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            get_java_file_list_from_root(fi_d, suffix, file_lists_dir)
        else:
            # if
            # print(os.path.join(filepath, fi_d))  # 打印的是单个java文件的绝对路径，因此这个循环会把单个repo里所有java文件打印
            data = os.path.join(filepath, fi_d) + "\n"
            fw = open(os.path.join(curDiry, file_lists_dir, "fileList_" + suffix + ".txt"), 'a+')
            fw.write(data)
            fw.close()


def get_trunc_file_path(file_lists_dir, suffix=""):
    curDir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(curDir, file_lists_dir, "fileList_" + suffix + ".txt")


def trunc_all_context(filePath):
    fw = open(filePath, 'a+')
    fw.truncate(0)
    fw.close()


def get_all_repos_absolute_from_a_group(group_dir):
    repo_absolute_dirs = os.listdir(group_dir)
    dir_num = len(repo_absolute_dirs)
    res = []
    reg = re.compile(r"\..*")
    for repo in repo_absolute_dirs:
        if reg.search(repo):
            continue
        str_res = group_dir + repo
        res.append(str_res)
    return res


def get_all_repo_name(group_dir):
    repo_names = os.listdir(group_dir)
    res = []
    reg = re.compile(r"\..*")
    for name in repo_names:
        if reg.search(name):
            continue
        res.append(name)
    return res


def wrt_all_repo_file_lists_txt(group_dir, repo_dirs, file_lists_dir="fileListsTest"):
    repo_names = get_all_repo_name(group_dir)
    length = len(repo_dirs)
    for i in range(length):
        path = get_trunc_file_path(file_lists_dir, repo_names[i])
        trunc_all_context(path)  # 为了覆写所有Java文件，必须清空上一次运行时的结果
        print("repo_dir: %s  >>>> repo name: %s" % (repo_dirs[i], repo_names[i]))
        get_java_file_list_from_root(repo_dirs[i], repo_names[i], file_lists_dir)


def get_file_lists_allinone(group_dir, file_lists_dir):
    repo_absolute_dirs = get_all_repos_absolute_from_a_group(group_dir)
    wrt_all_repo_file_lists_txt(group_dir, repo_absolute_dirs, file_lists_dir)


# 递归遍历目录下所有文件
if __name__ == "__main__":
    # get_file_lists_allinone("/Users/wangpei/workspace/")
    get_file_lists_allinone("/Users/wangpei/git-groups/", "fileListsFromGroupSDK")
    # curDir = os.path.dirname(os.path.realpath(__file__))
    # fileDir = os.path.join(curDir, "fileList.txt")
    # trunc_all_context(fileDir)
    # get_java_file_list_from_root('/Users/wangpei/workspace/')

