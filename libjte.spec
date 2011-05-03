# NOTE: current version of libjte is built from jigit.spec
# track both sources of libjte in case of future split
Summary:	Jigdo Template Extraction library
Summary(pl.UTF-8):	Biblioteka do szablonów jigdo (Jigdo Template Extraction)
Name:		libjte
Version:	0.1.1
%define	svnver	r861
Release:	0.%{svnver}.1
License:	LGPL v2.1+
Group:		Libraries
# svn co http://svn.openfmi.net/dev/people/danchev/jte libjte
Source0:	%{name}-%{version}-%{svnver}.tar.bz2
# Source0-md5:	033113f090da1ca9e9ac1398721d3d96
URL:		http://libburnia-project.org/
BuildRequires:	SEE-jigit.spec
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jigdo Template Extraction library.

%description -l pl.UTF-8
Biblioteka do szablonów jigdo (Jigdo Template Extraction).

%package devel
Summary:	Header files for JTE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki JTE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	zlib-devel

%description devel
Header files for JTE library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki JTE.

%package static
Summary:	Static JTE library
Summary(pl.UTF-8):	Statyczna biblioteka JTE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static JTE library.

%description static -l pl.UTF-8
Statyczna biblioteka JTE.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog doc/TODO
%attr(755,root,root) %{_libdir}/libjte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjte.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/{API,NOTES}
%attr(755,root,root) %{_libdir}/libjte.so
%{_libdir}/libjte.la
%{_includedir}/libjte
%{_pkgconfigdir}/libjte-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libjte.a
