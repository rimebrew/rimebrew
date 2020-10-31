from rimebrew.rimebrew import main
if __name__ == '__main__':
    """
    To future self:
    Back to the days, when the py community was building a package
    manager (pip & pypi), they introduced a mechanism called
    "relative path import". 

    Py scripts then divided into two types, user scripts which
    use regular imports and package scripts which use relative
    imports. HOWEVER, the relative imports doesn't designed very
    well, resulting this fucking stupid workaround.

    <https://pyinstaller.readthedocs.io/en/stable/operating-mode.html>

    """
    main()