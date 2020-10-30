#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Inspector.py define several "look up" functions
# It won't modify any file.
# For the stupid windows' terminal
from . import colorama
from .utility_functions import load_from_yamlfile, RimePaths
import os

colorama.init()

import typing

# TODO FIXME Implement abs path now!
meta_bundle = load_from_yamlfile(RimePaths.meta_bundle_yaml)
user_yaml = load_from_yamlfile(RimePaths.user_profile_yaml)
default_custom_yaml = load_from_yamlfile(RimePaths.default_custom_yaml)


def get_installed() -> typing.Set:
    return set(user_yaml['installed'])


def my_align(_string, _length, _type='L') -> str:
    """
        中英文混合字符串对齐函数
        This segment of py code is very rare that no one know who first write it!
    """
    _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
    for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
        if u'\u4e00' <= _char <= u'\u9fa5':  # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
            _str_len += 1
    _space = _length - _str_len  # 计算需要填充的空格数
    if _type == 'L':  # 根据对齐方式分配空格
        _left = 0
        _right = _space
    elif _type == 'R':
        _left = _space
        _right = 0
    else:
        _left = _space // 2
        _right = _space - _left
    return ' ' * _left + _string + ' ' * _right


# Some language use a very different char length.
def print_schemas():
    formatString = "{id:<20}{name}{status:<12}"
    print(formatString.format(id="# ID", name=my_align("# Name", 20), status="# Status"))
    for _id, schema in meta_bundle.items():
        installed = get_installed()
        status = colorama.Fore.BLUE + 'Installed' + colorama.Style.RESET_ALL if _id in installed else colorama.Fore.MAGENTA + 'Available' + colorama.Style.RESET_ALL
        print(formatString.format(id=_id, name=my_align(schema['display_name'], 20), status=status))

