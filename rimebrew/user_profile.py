from .utility_functions import load_from_yamlfile, RimePaths, dump_yaml


# functionalities of user_profile.yaml
# + track what user installed
# + some log
# + debug info

class user_profile(object):
    def __init__(self, path=RimePaths.user_profile_yaml):
        self._path = path
        self.user_profile = load_from_yamlfile(path)

    def get_installed_schema(self) -> list:
        return self.user_profile["installed"]

    def insert_new_schema(self, _schema_name) -> None:
        self.user_profile.append(_schema_name)
        dump_yaml(str(self.user_profile), self._path)

    def uninstall_schema(self, _schema_name) -> None:
        pass
