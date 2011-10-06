%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pystatsd
Version:        0.1.7
Release:        1%{?dist}
Summary:        Python implementation of the Statsd client/server
Group:          Applications/Internet
License:        Unknown
URL:            http://pypi.python.org/pypi/pystatsd/
Source0         http://pypi.python.org/packages/source/p/pystatsd/pystatsd-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
%if 0%{?fedora} && 0%{?fedora} < 13
BuildRequires:  python-setuptools-devel
%else
BuildRequires:  python-setuptools
%endif


%description
pystatsd is a client and server implementation of Etsy's brilliant statsd
server, a front end/proxy for the Graphite stats collection and graphing server.

* Graphite
    - http://graphite.wikidot.com
* Statsd
    - code: https://github.com/etsy/statsd
    - blog post: http://codeascraft.etsy.com/2011/02/15/measure-anything-measure-everything/

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/etc/init.d
install -m0755 redhat/pystatsd.init  %{buildroot}/etc/init.d/pystatsd
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*
/usr/bin/pystatsd-server
/etc/init.d/pystatsd

%changelog
* Thu Oct 07 2011 Sharif Nassar <sharif@mediatemple.net> - 0.1.7-1
- Initial package
