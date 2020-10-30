# installer
import os
from shutil import copy as Install
from .bundle import bundle_factory_from_schema_id
from .utility_functions import RimePaths


# TODO now, lets only install on the user's dir -> maybe yes? For portabilty
# 按照这个完美定义 user_data_dir https://github.com/rime/plum/blob/master/scripts/frontend.sh

# download from the main repo
# Project name convection:
# repo -> bundle -> single schema for each input method
# all the files goes into cache

# FIXME still some ulgy usage here
# TODO implement @dataclass schema
def basic_install(schema_id: str):

    _bundle = bundle_factory_from_schema_id(schema_id)
    _bundle.fetch()

    [Install(os.path.join(RimePaths.rimebrew_dir, 'cache', _bundle.repo.id, x), RimePaths.usr_data_dir)
     for x in _bundle.provides[schema_id]['files']]
    # TODO modify user_profile.yaml
