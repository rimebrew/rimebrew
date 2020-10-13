from dataclasses import dataclass
from typing import Dict, List

from utility_functions import load_yaml_doc


# A super _elegant_ YAML <-> bundle.yaml mapping

@dataclass
class Repository:
    id: str
    display_name: str
    url: str
    url_to_file: str

    def asb_url(self) -> str:
        return self.url + self.url_to_file


@dataclass
class Bundle:
    repo: Repository
    provides: List[Dict]


def bundle_factory(_bundle_file_path: str) -> Bundle:
    """
    Factory Method to construct a internal used Bundle object
    """
    [repo, recipes] = load_yaml_doc(_bundle_file_path)

    return Bundle(
        repo=Repository(
            id=repo['id'],
            display_name=repo['display_name'],
            url=repo['url'],
            url_to_file=repo['url_to_file']),
        provides=recipes)


if __name__ == "__main__":
    x = bundle_factory('./test.yaml')

    print(x.repo.id)
    print(x.repo.display_name)
    print(x.provides['luna_pinyin'])
