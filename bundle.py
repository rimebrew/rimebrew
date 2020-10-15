import os
from dataclasses import dataclass
from typing import Dict

from utility_functions import load_from_yamlfile, load_yaml_doc, fetch_zip_file_to


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
        fetch_zip_file_to(self.repo.url + self.repo.url_to_file, './cache/bundles',folder_name=self.repo.id)


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
    source_file = load_from_yamlfile('./cache/bundle_meta.yaml')[_schema_id]['source']
    return bundle_factory(os.path.join('./cache/rime_bundle', source_file))


if __name__ == "__main__":
    x = bundle_factory('./test.yaml')

    print(x.repo.id)
    print(x.repo.display_name)
    print(x.provides)
