# -*- coding: UTF-8 -*-

# Fetch bundles from cloud and then update bundle_meta

from utility_functions import *


def update():
    mkdir('./cache')
    os.chdir('./cache')
    main_bundle_dir = './rime_bundle'

    central_url = "https://github.com/rimebrew/rime_bundle/archive/main.zip"
    fetch_zip_file_to(central_url, '.', folder_name="rime_bundle")

    # get bundle list
    bundle_list = []
    for _file in os.listdir(main_bundle_dir):
        if _file[-5:] == ".yaml":
            bundle_list.append(_file)

    # This meta file is intended to simplify the GUI dev.
    meta_bundle = dict()

    for bundle_name in bundle_list:
        bundle = load_from_yamlfile(main_bundle_dir + '/' + bundle_name)
        for _name, schema in bundle['provides'].items():  # here, the items can be replaced by an iterator!
            schema['source'] = bundle_name
            meta_bundle[_name] = schema

    dump_yaml(meta_bundle, './bundle_meta.yaml')
