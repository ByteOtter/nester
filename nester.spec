#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define skip_python39 1

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define oldpython python
%{?sle15_python_module_pythons}
Name:           nester
Version:        1.1.1
Release:        0
Summary:        Create project structures for your Python, C, C++, CS, Java and Ruby projects
License:        GPL-3.0
URL:            https://www.github.com/ByteOtter/nester
Source0:        nester-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  %{python_module setuptools >= 65.5.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module click >= 8.1.3}
BuildRequires:  %{python_module pytest >= 6.2.4}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module questionary >= 1.10.0}
BuildRequires:  python-rpm-macros >= 20210929
BuildRequires:  fdupes
Requires:       python-click >= 8.1.3
Requires:       python-questionary >= 1.10.0

%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%if %{?suse_version} < 1500
BuildRequires:  python
%endif
%python_subpackages

%description
Create project structures for your Python, C, C++, CS, Java and Ruby projects.

%package doc
Summary:        Nester Documentation
Requires:       %{name} = %{version}

%description doc
Create project structures for your Python, C, C++, CS, Java and Ruby projects.

%prep
%autosetup -p1 -n nester-%{version}

%build
cp -r %{_sourcedir}/nester-%{version}/.git %{_builddir}/nester-%{version}
%pyproject_wheel
# cd docs && make html

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nester
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative nester

%post
%python_install_alternative nester

%postun
%python_uninstall_alternative nester

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/nester
%{_bindir}/nester-%{python_bin_suffix}
%{python_sitelib}/nester
%{python_sitelib}/nester_struct-%{version}.dist-info

%files %{python_files doc}
