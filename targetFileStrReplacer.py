#!/usr/bin/python
# -*- coding: utf-8 -*-
import linesCommentMaker as lcm
import re


def test_replace_without_read_write_together(file_path, str_tar, str_replace):
    found = False
    with open(file_path, "r+") as fr:
        content = fr.read()
        if str_tar in content:
            found = True
            print("found %s" % str_tar)
            new_ct = content.replace(str_tar, str_replace)
        else:
            print("target str \"%s\" not found" % str_tar)
    if found:
        with open(file_path, "w+") as fw:
            fw.write(new_ct)
            print("replaced %s with %s" % (str_tar, str_replace))
    return


def test_replace_within_line(file_path, str_tar, str_replace):
    with open(file_path, "r+") as fr:
        lines = fr.readlines()
    found = False
    line_cnt = 0
    line_concate = ""
    reg = re.compile(r"\s*\\\\|\s*#")
    for line in lines:
        line_cnt += 1
        if str_tar in line and reg.match(line) is None:
            found = True
            print("found %s at line %d" % (str_tar, line_cnt))
            line_replace_copy = line.replace(str_tar, str_replace)
            line_concate += line_replace_copy
        else:
            line_concate += line
    if found:
        with open(file_path, "w") as fw:
            fw.write(line_concate)
    else:
        print("target str \"%s\" not found" % str_tar)


def replace_tar_str_allinone_print(file_path, str_tar, str_replace, button=False):
    with open(file_path, "r+") as fr:
        lines = fr.readlines()
    found = False
    line_cnt = 0
    line_concate = ""
    reg = re.compile(r"\s*//|\s*#")
    for line in lines:
        line_cnt += 1
        if str_tar in line and reg.match(line) is None:
            found = True
            if button:
                print("found %s at line %d" % (str_tar, line_cnt))
            # lcm.make_line_comment(file_path, line_cnt)
            line_cmt = lcm.get_line_comment_str(file_path, line)
            line_concate += line_cmt
            line_replace_copy = line.replace(str_tar, str_replace)
            line_concate += line_replace_copy
            line_cnt += 1
        else:
            line_concate += line
    if found:
        with open(file_path, "w") as fw:
            fw.write(line_concate)
    else:
        if button:
            print("target str \"%s\" not found" % str_tar)


if __name__ == "__main__":
    # test_replace_within_line("test", "wangpei", "jude")
    replace_tar_str_allinone_print("test", "wangpei", "jude", True)
