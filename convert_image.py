#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : LoL_lang_modificaton
# @File    : convert_image.py
# @Author  : lee sure
# @Descriptions : convert images to python file
# @Date    : 2023/7/5 15:45 
# @Software : PyCharm


import base64

# convert image to python code.
def pic2py(picture_names, py_name):
    write_data = []
    for picture_name in picture_names:

        print(picture_name)
        filename = picture_name.replace(".\\img\\", "")
        filename = filename.replace(".", "_")
        with open("%s" % picture_name, 'rb') as r:
            b64str = base64.b64encode(r.read())
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    with open(f'{py_name}.py', 'w+') as w:
        for data in write_data:
            w.write(data)


pics = [r".\img\league_of_legends_alt_macos_bigsur_icon_190029.ico",
        r".\img\china_icon_127906.ico",
        r".\img\taiwan_icon_127914.ico",
        r".\img\krsouthkoreaflag_111691.ico",
        r".\img\australia_icon_127744.ico"]
# pics = [r".\img\china_icon_127906.ico"]
# Write the images in pics to image.py
pic2py(pics, 'image')
print("finishing converting...")
