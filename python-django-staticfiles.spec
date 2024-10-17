%define realname    django-staticfiles
%define name	    python-%{realname}
%define version 0.3.2
%define release 2

Name: %{name}
Version: 1.2.1
Release: 2
Summary:        A Django app that provides helpers for serving static files
Group:          Development/Python
License:        BSD
URL:            https://bitbucket.org/jezdez/django-authority/
Source:         https://pypi.python.org/packages/source/d/django-staticfiles/django-staticfiles-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
A Django app that provides helpers for serving static files

%prep
%setup -q -n %{realname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*



%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 591974
- import python-django-staticfiles


