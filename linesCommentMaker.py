#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

test_dir = "/Users/wangpei/git-groups/AliSourcingImage/gradle/wrapper/gradle-wrapper.properties"


def make_line_comment(file_path, line_num):
    with open(file_path, "r+") as fr:
        lines = fr.readlines()
    line_cnt = 0
    line_concate = ""
    for line in lines:
        line_cnt += 1
        if line_cnt == line_num and "//" not in line:
            line_replace_copy = get_line_comment_str(file_path, line)
            line_concate += line_replace_copy
        else:
            line_concate += line
    with open(file_path, "w") as fw:
        fw.write(line_concate)


def make_lines_comment(file_path, line_list_):
    for li in line_list_:
        make_line_comment(file_path, li)


def get_file_path_lines(file_path):
    with open(file_path, "r") as fr:
        lines = fr.readlines()
    return lines


def find_content_str_line_num(lines, content_str):
    line_cnt = 0
    res = []
    found = False
    reg = re.compile(r"\s*//|\s*#")
    for line in lines:
        line_cnt += 1
        if content_str in line and reg.match(line) is None:
            found = True
            res.append(line_cnt)
    if found:
        # print("found str %s in not-comment lines, first at line %d" % (content_str, res[0]))
        return res[0]
    else:
        pass
        # print("not found str %s in not-comment lines" % content_str)


def get_line_comment_str(file_path, line):
    if ".gradle" in file_path and "settings" not in file_path:
        return "// " + line
    elif ".properties" in file_path:
        return "# " + line
    else:
        return "//" + line


if __name__ == "__main__":
    make_line_comment("test", 3)
    line_list = [1, 2, 3, 4, 5]
    make_lines_comment("test", line_list)
    lins_src = get_file_path_lines("test")
    print(find_content_str_line_num(lins_src, "wangpei"))
