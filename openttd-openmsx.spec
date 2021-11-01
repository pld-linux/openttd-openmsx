Summary:	OpenMSX is an open source base music set for OpenTTD
Summary(pl.UTF-8):	OpenMSX jest podstawowym, otwartoźródłowym zestawem muzyki dla OpenTTD
Name:		openttd-openmsx
Version:	0.4.2
Release:	2
License:	GPL v2+
Group:		Applications/Games
Source0:	https://cdn.openttd.org/openmsx-releases/%{version}/openmsx-%{version}-source.tar.xz
# Source0-md5:	3741ec7b1370690d0bcf412e2531553a
URL:		http://wiki.openttd.org/OpenMSX
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRequires:	xz
Requires:	openttd-data >= 1.0.0
Requires:	TiMidity++
Requires:	TiMidity++-instruments
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMSX is an open source base music set for OpenTTD.

%description -l pl.UTF-8
OpenMSX jest podstawowym, otwartoźródłowym zestawem muzyki dla
OpenTTD.

%prep
%setup -q -n openmsx-%{version}-source

%build
%{__make} bundle

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR="$RPM_BUILD_ROOT%{_datadir}/openttd/baseset" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog.txt,readme.txt}
%dir %{_datadir}/openttd/baseset
%{_datadir}/openttd/baseset/openmsx-%{version}
