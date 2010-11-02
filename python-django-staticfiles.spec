%define realname    django-staticfiles
%define name	    python-%{realname}
%define version 0.3.2
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A Django app that provides helpers for serving static files
Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/jezdez/django-authority/
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*

