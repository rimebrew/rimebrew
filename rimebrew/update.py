# -*- coding: UTF-8 -*-

# Fetch bundles from cloud and then update bundle_meta
import os
from .bundle import bundle_factory
from .utility_functions import *


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

if __name__ == "__main__":
    update()
