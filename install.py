# installer
import os
from shutil import copy as Install

import bundle

# TODO now, lets only install on the user's dir -> maybe yes? For portabilty
# TODO 按照这个完美定义 user_data_dir https://github.com/rime/plum/blob/master/scripts/frontend.sh
user_data_dir = os.path.relpath('../')


# TODO Code below are meant to be used for so that Homebrew & Linux can install in any location.
# mode ='dev'
# if (mode == 'dev'):
#     mkdir('./user_data_dir')
#     user_data_dir = os.path.abspath("./user_data_dir")
# if sys.platform.startswith('linux'):
#     user_data_dir=
# elif sys.platform.startswith('darwin'):
#     pass
# elif sys.platform.startswith('win32'):
#     pass


# download from the main repo
# Project name convection:
# repo -> bundle -> single schema for each input method
# all the files goes into cache


def basic_install(schema_id: str):
    # TODO 😎😎😎
    #
    #
    _bundle = bundle.Bundle(schema_id)
    [Install(x, user_data_dir) for x in _bundle.dict_abs_files]
    [Install(x, user_data_dir) for x in _bundle.schema.file_abs_locations]
