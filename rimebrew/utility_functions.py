import io
import os
import shutil
import tempfile
import typing
import urllib.request
import zipfile
from os.path import expanduser
from pathlib import Path

from . import yaml

# mode = 'dev'

# commonly used functions

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


def dump_yaml(_content: str, _path: str):
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
def _usr_data_dir():
    if 'ibus' in [os.getenv('INPUT_METHOD'), os.getenv('GTK_IM_MODULE')]:
        return home+"/.config/ibus/rime/"
    elif "fcitx" in [os.getenv('INPUT_METHOD'), os.getenv('QT_IM_MODULE')]:  # TODO not sure
        return home+"/.config/fcitx/rime/"
    elif "fcitx5" in [os.getenv('INPUT_METHOD'), os.getenv('QT_IM_MODULE')]:
        return home+"/.local/share/fcitx5/rime"
    elif os.name == "darwin":
        return "~/Library/Rime/"
    elif os.name == "Windows":
        print("Detected that you are using Windows.\n")
        print("Please move rimebrew executable inside your user config dir")
        return "../"


def usr_data_dir()->str:
    """ wrapper of _usr_data_dir """
    udr = _usr_data_dir()
    mkdir(udr)
    return udr

def rimebrew_dir()->str:
    rbd = os.path.join(usr_data_dir(), 'rimebrew')
    mkdir(rbd)
    return rbd

