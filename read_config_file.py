#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : LoL_lang_modificaton
# @File    : read_config_file.py
# @Author  : lee sure
# @Descriptions : read lol configuration file
# @Date    : 2023/7/4 18:14 
# @Software : PyCharm
import os
import subprocess

directory = r'C:\ProgramData\Riot Games'
extension = '.yaml'


def find_files(directory, extension):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files


def read_conf_file(file):
    with open(file, 'r') as f:
        files_content = f.readlines()
    return files_content

# ko_KR zh_CN zh_TW en_AU
def modify_file(lang="zh_CN"):
    files = find_files(directory, extension)
    files_content = read_conf_file("img/league_of_legends.live.product_settings.yaml")
    # modify the lang
    new_contents = [content for content in files_content]
    print(new_contents)
    for new_content in new_contents:
        if ("locale:" in new_content.strip()) and (new_content.strip().startswith("locale:", 0)):
            new_contents[new_contents.index(new_content)] = '    locale: "'+lang+'"\n'
    print(new_contents)
    for file in files:
        ori_file = file
        if r"product_settings" in file:
            os.remove(file)
        if r"product_settings" not in file:
            new_file = [c for c in ori_file.split("\\")]
            new_file[len(new_file) - 2] = "league_of_legends.live"
            new_file[len(new_file) - 1] = "league_of_legends.live.product_settings.yaml"
            new_file = "\\".join(new_file)
            print(new_file)
            with open(new_file, 'w') as fi:
                for content in new_contents:
                    fi.write(content)
    print("--write successfully, please restart your client--")

# "E:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live
def start_lol(app_path=r"E:\Riot Games\Riot Client\RiotClientServices.exe", arguments=None):
    if arguments is None:
        arguments = ['--launch-product', 'league_of_legends', '--launch-patchline', 'live']
    subprocess.run([app_path]+arguments, shell=True, check=True)

if __name__ == "__main__":
    modify_file()
    start_lol()