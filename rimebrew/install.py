# installer
import os
from shutil import copy as Install
from .bundle import bundle_factory_from_schema_id
from .utility_functions import RimePaths, load_from_yamlfile


def basic_install(schema_id: str):
    """
    copy two files then paste type of install.
    update user profile.
    """
    _bundle = bundle_factory_from_schema_id(schema_id)
    _bundle.fetch()

    [Install(os.path.join(RimePaths.rimebrew_dir, 'cache', _bundle.repo.id, x), RimePaths.usr_data_dir)
     for x in _bundle.provides[schema_id]['files']]
    # TODO modify user_profile.yaml
