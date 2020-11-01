# Improve this file if you know things about make
all: gen_translates
	python3 setup.py sdist bdist_wheel
	yes | pip uninstall rime_brew
	pip install ./dist/rime_brew-0.0.8-py3-none-any.whl
	rimebrew

pypi_build:
	python3 setup.py sdist bdist_wheel

pypi_upload:
	python3 -m twine upload --repository pypi dist/*

pip_essentials:
	pip install wheel

pip_remove:
	pip uninstall rime-brew

# windows
win_dist:
	python3.exe  .\pyinstaller_dist.py  

win_dist_raw:
	pyinstaller importer.py --name rimebrew --exclude-module tkinter --noconfirm --onefile --console

# macos
mac_dist_cxfreeze:
	python3 ./setup_mac_cxfreeze.py bdist_mac

clean:
	rm -rf build dist

gen_translates:
	msgfmt -o ./rimebrew/local/zh_CN/LC_MESSAGES/messages.mo ./rimebrew/local/zh_CN/LC_MESSAGES/messages.po
