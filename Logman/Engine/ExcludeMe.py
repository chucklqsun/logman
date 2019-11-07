from Logman.Config.Exclude import Exclude
from Logman.Config.Settings import Settings
from Logman.Utility.File import *
from Logman.GlobalConfig import GlobalConfig
from pathlib import Path
import os
import re


def get_exclude_replace_pattern_list():
    ret = []
    for i in Exclude.Exclude_replace_pattern:
        pattern = r"%s" % i[0]
        regex = re.compile(pattern, re.IGNORECASE)
        ret.append([regex, i[1]])
    return ret


def get_exclude_file():
    glob_path = Path(r"%s" % GlobalConfig.app_path)
    file_list = [str(pp) for pp in glob_path.glob("**/%s*" % Settings.prefix["old_exclude_prefix"])]
    print("\nReading exclude file:")
    print(file_list)
    return file_list


def pre_exclude_log(ori_content):
    pre_content = []
    for level in Settings.filter_level:
        for ln in ori_content:
            if ln.isspace():
                continue
            if re.search(r"\b%s\b" % level, ln):
                pre_content.append(ln)
    return pre_content


def post_exclude_log(pre_content):
    post_content = []
    exclude_file_list = get_exclude_file()
    merged_file = []
    # merge all exclude files
    for f in exclude_file_list:
        merged_file += read_file(f)

    exclude_regex_list = get_exclude_replace_pattern_list()
    for i in range(0, len(pre_content)):
        waive_flag = False
        ln = pre_content[i]

        # firstly replace dynamic string
        for e in exclude_regex_list:
            ln = e[0].sub(e[1], ln)

        # check if line in exclude file
        for exclude_ln in merged_file:
            if exclude_ln == ln:
                waive_flag = True

        if not waive_flag:
            post_content.append(pre_content[i])

    return post_content


def output_new_exclude_file(post_content):
    path = GlobalConfig.app_path
    exclude_lines = []
    exclude_regex_list = get_exclude_replace_pattern_list()
    for ln in post_content:
        for e in exclude_regex_list:
            ln = e[0].sub(e[1], ln)
        exclude_lines.append(ln)

    exclude_lines = list(dict.fromkeys(exclude_lines))
    file_path = os.path.join(path, 'output', Settings.prefix["new_exclude_prefix"] + ".txt")
    print("\nOutput new exclude file %s" % file_path)
    write_file("".join(exclude_lines), file_path)