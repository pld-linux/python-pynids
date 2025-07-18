%define 	module	pynids
Summary:	Python wrapper for libnids, a Network Intrusion Detection System library
Summary(pl.UTF-8):	Pythonowe obudowanie libnids - systemu wykrywania intruzów w sieci
Name:		python-%{module}
Version:	0.6.2
Release:	1
# module itself is GPL v2+, but libnids is GPL v2 only
License:	GPL v2
Group:		Development/Languages/Python
##Source0Download: https://jon.oberheide.org/pynids/ (up to 0.6.1
#Source0:	https://jon.oberheide.org/files/pynids-%{version}.tar.gz
#Source0Download: https://pypi.org/simple/pynids/
Source0:	https://files.pythonhosted.org/packages/source/p/pynids/pynids-%{version}.tar.gz
# Source0-md5:	6f2a15ee393beec4c9d6ce65f869a58c
Patch0:		%{name}-build.patch
Patch1:		%{name}-libnet.patch
URL:		https://jon.oberheide.org/pynids/
BuildRequires:	libnet-devel >= 1:1.1
BuildRequires:	libpcap-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pynids is a Python wrapper for libnids, a Network Intrusion Detection
System library offering sniffing, IP defragmentation, TCP stream
reassembly and TCP port scan detection. Let your own Python routines
examine network conversations.

%description -l pl.UTF-8
pynids to pythonowe obudowanie libnids - biblioteki systemu wykrywania
intruzów w sieci (Network Intrusion Detection System), oferującej
snifowanie, defragmentację IP, rekonstrukcję strumienia TCP oraz
wykrywanie skanowania portów TCP. Moduł pozwala na sprawdzanie
komunikacji w sieci z poziomu Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{py_sitedir}/nidsmodule.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pynids-%{version}-py*.egg-info
%endif
