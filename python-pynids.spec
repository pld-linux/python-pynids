%define 	module	pynids
Summary:	Python wrapper for libnids, a Network Intrusion Detection System library
Name:		python-%{module}
Version:	0.6.1
Release:	3
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://jon.oberheide.org/pynids/downloads/pynids-%{version}.tar.gz
# Source0-md5:	6ce600d0130b0feec9a3797a27825d15
URL:		http://jon.oberheide.org/pynids/
BuildRequires:	glib2-devel
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pynids is a Python wrapper for libnids, a Network Intrusion Detection
System library offering sniffing, IP defragmentation, TCP stream
reassembly and TCP port scan detection. Let your own Python routines
examine network conversations.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Example
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pynids-*.egg-info
%endif
