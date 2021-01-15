import io
import os
import shutil
import tempfile
import urllib.request
import zipfile
import typing

from os.path import expanduser
from pathlib import Path
from dataclasses import dataclass
from typing import Dict

import colorama
import yaml

colorama.init()

# -----------------------------------------------------------------------------
# TODO List
# -----------------------------------------------------------------------------

# Move dir related to rimebrew.py (cli)

# -----------------------------------------------------------------------------
# Common Data structures
# -----------------------------------------------------------------------------

# A super _elegant_ YAML <-> bundle.yaml mapping

@dataclass
class Repository:
    id: str
    display_name: str
    url: str
    url_to_file: str

    @property
    def asb_url(self) -> str:
        return self.url + self.url_to_file


@dataclass
class Bundle:
    repo: Repository
    provides: Dict

    def fetch(self):
        fetch_zip_file_to(self.repo.url + self.repo.url_to_file, os.path.join(RimePaths.rimebrew_dir, "cache"),
                          folder_name=self.repo.id)
        print("fetch sucessfully")


## TODO here we need some magic! Turn a str into a CLASS :)

def bundle_factory(_bundle_file_path: str) -> Bundle:
    """
    Factory Method to construct a internal used Bundle object
    """
    bundle = load_yaml_doc(_bundle_file_path)[0]

    return Bundle(
        repo=Repository(
            id=bundle['id'],
            display_name=bundle['display_name'],
            url=bundle['url'],
            url_to_file=bundle['url_to_file']),
        provides=bundle['provides'])


def bundle_factory_from_schema_id(_schema_id: str, fetch=True) -> Bundle:
    bundle_source_file = load_from_yamlfile(RimePaths.meta_bundle_yaml)[_schema_id]['source']
    return bundle_factory(os.path.join(os.path.join(RimePaths.rimebrew_dir, "rime_bundle"), bundle_source_file))

# -----------------------------------------------------------------------------
# Commonly used functions
# -----------------------------------------------------------------------------

def mkdir(_path: 'str'):
    Path(_path).mkdir(parents=True, exist_ok=True)


def download_url_to_path(url: str, destination_path: str):
    with urllib.request.urlopen(url) as dl_file:
        with open(destination_path, 'wb') as out_file:
            out_file.write(dl_file.read())


def download_url_to_file(url: str, file: io.TextIOWrapper):
    with urllib.request.urlopen(url) as dl_file:
        file.write(dl_file.read())


def fetch_zip_file_to(url: str, dest_dir: str, folder_name=None):
    mkdir(dest_dir)
    temp = tempfile.TemporaryFile()
    download_url_to_file(url, temp)

    with zipfile.ZipFile(temp, 'r', ) as myzip:
        _main_name = myzip.namelist()[0]
        for file in myzip.namelist():
            if file.startswith(_main_name):
                myzip.extractall(path=dest_dir)
    if folder_name is not None:
        if os.path.exists(dest_dir + '/' + folder_name): shutil.rmtree(dest_dir + '/' + folder_name)
        os.rename(dest_dir + '/' + _main_name, dest_dir + '/' + folder_name)


def load_from_yamlfile(_path: str) -> typing.Union[list, dict]:
    with open(_path, 'r') as yaml_config_file:
        return yaml.load(yaml_config_file, Loader=yaml.Loader)


def load_yaml_doc(_path: str):
    with open(_path, 'r') as file:
        return [document for document in yaml.load_all(file, Loader=yaml.Loader)]


def dump_yaml(_content, _path: str):
    with open(_path, 'wb') as _file:
        _file.write(yaml.dump(_content, allow_unicode=True).encode())


# PYTHON

def strJoin(*strings):
    return ''.join(strings)


# RIME related


# usr_data_dir discovery
# avoid <https://github.com/rime/plum/issues/2>

# fcitx code copy from https://github.com/rime/plum/blob/master/scripts/frontend.sh#L30
# assuming it ir right

home = expanduser("~")


class _rimePaths:
    def _usr_data_dir(self):
        """
        按照这个完美定义 user_data_dir https://github.com/rime/plum/blob/master/scripts/frontend.sh
        """
        if 'ibus' in [os.getenv('INPUT_METHOD'), os.getenv('GTK_IM_MODULE')]:
            return home + "/.config/ibus/rime/"
        elif "fcitx" in [os.getenv('INPUT_METHOD'), os.getenv('QT_IM_MODULE')]:  # TODO not sure
            return home + "/.config/fcitx/rime/"
        elif "fcitx5" in [os.getenv('INPUT_METHOD'), os.getenv('QT_IM_MODULE')]:
            return home + "/.local/share/fcitx5/rime"
        elif os.name == "darwin":
            return "~/Library/Rime/"
        elif os.name == "Windows":
            print("Detected that you are using Windows.\n")
            print("Please move rimebrew executable inside your user config dir")
            return "../"

    @property
    def usr_data_dir(self) -> str:
        """ wrapper of _usr_data_dir """
        udr = self._usr_data_dir()
        mkdir(udr)
        return udr

    @property
    def rimebrew_dir(self) -> str:
        rbd = os.path.join(self.usr_data_dir, 'rimebrew')
        mkdir(rbd)
        return rbd

    @property
    def meta_bundle_yaml(self) -> str:
        return os.path.join(self.rimebrew_dir, 'bundle_meta.yaml')

    @property
    def user_profile_yaml(self) -> str:
        return os.path.join(self.rimebrew_dir, 'user_profile.yaml')

    @property
    def default_custom_yaml(self) -> str:
        return os.path.join(self.usr_data_dir, "default.custom.yaml")


RimePaths = _rimePaths()

# -----------------------------------------------------------------------------
# Inspector: functions related to display internal info.
# -----------------------------------------------------------------------------




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

# -----------------------------------------------------------------------------
# updates
# -----------------------------------------------------------------------------
# Fetch bundles from cloud and then update bundle_meta

def update():
    os.chdir(RimePaths.rimebrew_dir)
    main_bundle_dir = os.path.join('./rime_bundle')

    central_url = "https://github.com/rimebrew/rime_bundle/archive/main.zip"
    fetch_zip_file_to(central_url, '.', folder_name="rime_bundle")

    # get bundle list
    bundle_file_list = []
    for _file in os.listdir(main_bundle_dir):
        if _file[-5:] == ".yaml":
            bundle_file_list.append(_file)

    # le is intended to simplify the GUI dev.
    meta_bundle = dict()

    for bundle_file in bundle_file_list:

        bundle = bundle_factory(main_bundle_dir + '/' + bundle_file)
        for formula in bundle.provides:
            bundle.provides[formula]["source"] = bundle_file
            meta_bundle[formula] = bundle.provides[formula]

        dump_yaml(meta_bundle, './bundle_meta.yaml')


# -----------------------------------------------------------------------------
# User_profiles
# -----------------------------------------------------------------------------


# functionalities of user_profile.yaml
# + track what user installed
# + some log
# + debug info

class user_profile(object):
    def __init__(self, path=RimePaths.user_profile_yaml):
        self._path = path
        self.user_profile = load_from_yamlfile(path)

    def get_installed_schema(self) -> list:
        return self.user_profile["installed"]

    def insert_new_schema(self, _schema_name) -> None:
        self.user_profile.append(_schema_name)
        dump_yaml(str(self.user_profile), self._path)

    def uninstall_schema(self, _schema_name) -> None:
        pass


@dataclass
class enviroment:
    user_data_dir: str


@dataclass
class profile:
    _installed: list
    enviroment: enviroment


def user_profile() -> profile:
    profile_tree = load_from_yamlfile('./user_profile.yaml')
    return profile(
        installed=profile_tree['installed'],
        enviroment=enviroment(
            user_data_dir=load_from_yamlfile("./")
        )
    )


# -----------------------------------------------------------------------------
# Initialization
# -----------------------------------------------------------------------------
# TODO FIXME Implement abs path now!
update()
meta_bundle = load_from_yamlfile(RimePaths.meta_bundle_yaml)
# user_yaml = load_from_yamlfile(RimePaths.user_profile_yaml)
# default_custom_yaml = load_from_yamlfile(RimePaths.default_custom_yaml)
# user_profile_yaml = load_from_yamlfile(RimePaths.user_profile_yaml)

