Summary:	Open source replacement for the original Transport Tycoon Deluxe (TTD) music
Summary(pl.UTF-8):	Darmowy zastępnik dla oryginalnej muzki do gry Transport Tycoon Deluxe (TTD)
Name:		openttd-openmsx
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://bundles.openttdcoop.org/openmsx/releases/openmsx-%{version}-source.tar.gz
# Source0-md5:	f03e93d4818eaa6035c8e8f6056bbef1
URL:		http://wiki.openttd.org/OpenMSX
BuildRequires:	sed >= 4.0
Requires:	openttd-data
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMSX is an open source replacement for the original Transport
Tycoon Deluxe (TTD) music.

%description -l pl.UTF-8
Darmowy zastępnik dla oryginalnej muzki do gry Transport Tycoon Deluxe
(TTD).

%prep
%setup -q -n openmsx-%{version}-source
%{__sed} -i 's,$(INSTALL_DIR),$(DESTDIR)$(INSTALL_DIR),' scripts/Makefile.bundles

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR="%{_datadir}/openttd/gm" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog.txt,readme.txt}
%{_datadir}/openttd/gm/openmsx-%{version}
