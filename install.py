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

# FIXME still some ulgy usage here
# TODO implement @dataclass schema
def basic_install(schema_id: str):
    _bundle = bundle.bundle_factory_from_schema_id(schema_id)
    _bundle.fetch()

    [Install(os.path.join('./cache/bundles',_bundle.repo.id,x), user_data_dir)
            for x in _bundle.provides[schema_id]['files']]

    # TODO modify user_profile.yaml

if __name__ == "__main__":
    basic_install('arabic')
