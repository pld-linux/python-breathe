# NOTE: for versions >= 4.13 (for python3/Sphinx 2) see python3-breathe.spec
#
# Conditional build:
%bcond_without	tests	# nose tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-breathe.spec)

Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Name:		python-breathe
# NOTE: keep 4.12 here; 4.13+ requires Sphinx 2 and Python 3
Version:	4.12.0
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/michaeljones/breathe/releases
Source0:	https://github.com/michaeljones/breathe/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2288749c6e3b2fe1e527873e97144843
URL:		https://github.com/michaeljones/breathe
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.8
BuildRequires:	python-docutils >= 0.12
BuildRequires:	python-nose
BuildRequires:	python-six >= 1.9
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.8
BuildRequires:	python3-docutils >= 0.12
BuildRequires:	python3-nose
BuildRequires:	python3-six >= 1.9
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Breathe is an extension to reStructuredText and Sphinx to be able to
read and render the Doxygen XML output.

%description -l pl.UTF-8
Breathe to rozszerzenie do systemu dokumentacji reStructuredText i
Sphinx, pozwalające na odczyt i renderowanie wyjścia XML z Doxygena.

%package -n python3-breathe
Summary:	Sphinx Doxygen renderer
Summary(pl.UTF-8):	Renderer Doxygena dla systemu dokumentacji Sphinx
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-breathe
Breathe is an extension to reStructuredText and Sphinx to be able to
read and render the Doxygen XML output.

%description -n python3-breathe -l pl.UTF-8
Breathe to rozszerzenie do systemu dokumentacji reStructuredText i
Sphinx, pozwalające na odczyt i renderowanie wyjścia XML z Doxygena.

%prep
%setup -q -n breathe-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
cd tests
PYTHONPATH=.. \
nosetests-%{py_ver}
cd ..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd tests
PYTHONPATH=.. \
nosetests-%{py3_ver}
cd ..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/breathe-apidoc{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/breathe-apidoc{,-3}
ln -sf breathe-apidoc-3 $RPM_BUILD_ROOT%{_bindir}/breathe-apidoc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/breathe-apidoc-2
%{py_sitescriptdir}/breathe
%{py_sitescriptdir}/breathe-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-breathe
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/breathe-apidoc
%attr(755,root,root) %{_bindir}/breathe-apidoc-3
%{py3_sitescriptdir}/breathe
%{py3_sitescriptdir}/breathe-%{version}-py*.egg-info
%endif
