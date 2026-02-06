Summary:	The LessTif/Motif extension library
Summary(pl.UTF-8):	Biblioteka rozszerzeń do LessTifa/Motifa
Name:		Xlt
Version:	13.0.13
Release:	4
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://downloads.sourceforge.net/xlt/%{name}-%{version}.tar.gz
# Source0-md5:	46b6259c7637d6e9b87520eb91b6ea51
Patch0:		%{name}-format.patch
Patch1:		%{name}-types.patch
URL:		https://xlt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	motif-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LessTif/Motif extension library. This consists of several widgets
and convience functions to make LessTif, or if you must Motif,
programming more enjoyable.

%description -l pl.UTF-8
Biblioteka rozszerzeń do LessTifa/Motifa. Zawiera trochę widgetów i
funkcji żeby nieco uprzyjemnić programowanie z użyciem LessTifa czy
Motifa.

%package devel
Summary:	Xlt header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja Xlt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	motif-devel >= 1.2

%description devel
Xlt header files and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do Xlt.

%package static
Summary:	Xlt static library
Summary(pl.UTF-8):	Biblioteka statyczna Xlt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Xlt static library.

%description static -l pl.UTF-8
Biblioteka statyczna Xlt.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

touch MaintainerMode.am

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

# packaged as %doc in -devel
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/Xlt
# packaged in motif
%{__rm} $RPM_BUILD_ROOT%{_aclocaldir}/ac_find_motif.m4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libXlt.so.*.*.*
%ghost %{_libdir}/libXlt.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,gif}
%{_libdir}/libXlt.so
%{_libdir}/libXlt.la
%{_includedir}/Xlt
%{_aclocaldir}/ac_find_xlt.m4
%{_aclocaldir}/ac_find_xpm.m4
%{_mandir}/man3/StrokeInstall.3*
%{_mandir}/man3/Strokes.3*
%{_mandir}/man3/Xlt*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXlt.a
