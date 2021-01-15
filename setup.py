import setuptools

# Detailed info on best practice to package a click_ app:
# https://click.palletsprojects.com/en/7.x/setuptools/

print(setuptools.find_packages())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rime_brew",  # Replace with your own username
    version="0.0.8",
    author="slbtty",
    author_email="shenlebantongying@gmail.com",
    description="RIME schemas manager",
    long_description="RIME schema manager",
    long_description_content_type="text/markdown",
    url="https://github.com/rimebrew/rimebrew",
    install_requires=[
        'click',
        'colorama',
        'pyYAML'
    ],
    packages=setuptools.find_packages(),
    # translation list
    package_data={'rimebrew': ['local/zh_CN/LC_MESSAGES/messages.po','local/zh_CN/LC_MESSAGES/messages.mo']},
    entry_points='''
        [console_scripts]
        rimebrew=rimebrew.rimebrew:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
