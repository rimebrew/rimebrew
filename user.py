from dataclasses import dataclass

from .utility_functions import load_from_yamlfile

# currently this file only provide a installed list.

@dataclass
class enviroment:
    user_data_dir:str

@dataclass
class profile:
    _installed: list
    enviroment: enviroment

def user_profile() -> profile:
    profile_tree = load_from_yamlfile('./user_profile.yaml')
    return profile(
        installed=profile_tree['installed'],
        enviroment=enviroment(
            user_data_dir=load_from_yamlfile("./")
        )
    )

if __name__ == "__main__":
    x = user_profile()
    print(x.installed)
