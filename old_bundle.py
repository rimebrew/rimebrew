import os.path

from .utility_functions import load_from_yamlfile, fetch_zip_file_to

# Rename this file -> it contains all the data structures used
# local_index.yaml -> local_index -> to store all local datas
#
#
# I am not using OOP,
# the Class are only used as a data structure like C's struct with functions.

rime_bundle = './cache/rime_bundle'
bundle_dir = './cache/bundles'


# 这个 bundle 需要重构
# 通过继承 pyyaml.YAMLObject 直接解析成一个对象，而非一个字典集合
# 通过字典传递信息，总觉的不严谨
# 后面改一个名字，就要手动更新所有信息，没办法重构。

class Schema:
    """
    Description of a schema.

    """

    # FIXME 临时放进去的 PATH
    def __init__(self, _schema_id: set, _schema_yaml: dict, _mother_bundle: str):
        self._id = _schema_id
        self._mother_bundle = _mother_bundle
        self.YAML = _schema_yaml

    @property
    def files(self) -> list:
        return self.YAML['files']

    @property
    def file_abs_locations(self):
        # 😎
        return iter([os.path.abspath(bundle_dir + '/' + self._mother_bundle + '/' + file) for file in self.files])


class Bundle:
    # defined var : user user_data_dir
    def __init__(self, _schema_id):
        """
        Create bundle from schema_id -> possibly more way to create it?
        """
        meta_bundle = load_from_yamlfile('./cache/bundle_meta.yaml')
        self.bundle_file = meta_bundle[_schema_id]['source']

        # FIXME sort shits below :)
        self._schema_id = _schema_id  #
        self.YAML = load_from_yamlfile(rime_bundle + '/' + self.bundle_file)
        self.remote_url = self.YAML['repository']['url'] + self.YAML['repository']['url_to_file']
        self._dict = self.YAML['repository']['dict']
        self._bundle_id = self.YAML['repository']['id']
        self._provide = self.YAML['provides']

        self._objectdict = self.YAML['repository']['dict']

    def fetch_repo(self):
        fetch_zip_file_to(self.remote_url, bundle_dir, folder_name=self.YAML['repository']['id'])

    @property
    def dict_files(self) -> list:
        return self._dict

    @property
    def dict_abs_files(self) -> list:
        return [os.path.abspath(bundle_dir + "/" + self._bundle_id + "/" + x) for x in self._dict]

    # @property
    # def provides(self) -> list:
    #     pass

    def get_schema(self, _id) -> type(Schema):
        return Schema(_id, self._provide[_id])

    # 现在只有通过 schema_id 来定义，这里直接返回 请求bundle的 schema
    @property
    def schema(self):
        return Schema(self._schema_id, self._provide[self._schema_id], self._bundle_id)


# test
if __name__ == "__main__":
    arabic = Bundle('arabic')
    arabic.fetch_repo()
