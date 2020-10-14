from dataclasses import dataclass

from utility_functions import load_from_yamlfile


# currently this file only provide a installed list.

@dataclass
class profile:
    installed: list


def user_profile() -> profile:
    profile_tree = load_from_yamlfile('./user_profile.yaml')
    return profile(
        installed=profile_tree['installed']
    )


if __name__ == "__main__":
    x = user_profile()
    print(x.installed)
