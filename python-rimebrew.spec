#
# spec file for package python-rime_brew
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

# ref: https://build.opensuse.org/package/view_file/openSUSE:Factory/youtube-dl/python-youtube-dl.spec?expand=1 
# ref https://en.opensuse.org/openSUSE:Packaging_Python
# ref https://openbuildservice.org/help/manuals/obs-user-guide/art.obs.bg.html

%define skip_python2 1 
Name:           python-rime_brew
Version:        0.0.7
Release:        0
License:        SUSE-Public-Domain AND CC-BY-SA-3.0
Summary:        RIME schemas manager
Url:            https://github.com/rimebrew/rimebrew
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/r/rime_brew/rime_brew-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
RIME schemas manager

%prep
%setup -q -n rime_brew-%{version}

%build
%python_build

%install
%python_install

# code below is deleting the build dirs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%python3_only %{_bindir}/rimebrew
%{python_sitelib}/*

%changelog
