import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=rimebrew',
    '--exclude-module=tkinter',
    '--exclude-module=six',
    '--onefile',
    '--noconfirm',
    '--console',
    './importer.py'
])