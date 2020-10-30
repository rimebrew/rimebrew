# Improve this file if you know things about make
all:
	python3 setup.py sdist bdist_wheel
	yes | pip uninstall rime_brew
	pip install ./dist/rime_brew-0.0.8-py3-none-any.whl
	rimebrew

pypi_build:
	python3 setup.py sdist bdist_wheel
pypi_upload:
	python3 -m twine upload --repository pypi dist/*

clean:
	rm -rf ./dist

remove:
	pip uninstall rime-brew