Summary:	The LessTif extension library
Summary(pl):	Biblioteka rozszerzeÒ do LessTifa
Name:		Xlt
Version:	9.0.9
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
BuildRequires:	lesstif-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lynx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The LessTif extension library. This consists of several widgets and
convience functions to make LessTif, or if you must Motif, programming
more enjoyable.

%description -l pl
Biblioteka rozszerzeÒ do LessTifa. Zawiera trochÍ widgetÛw i funkcji
øeby nieco uprzyjemniÊ programowanie z uøyciem LessTifa czy Motifa.

%package devel
Summary:	Xlt header files and development documentation
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja Xlt
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Xlt header files and development documentation.

%description devel -l pl
Pliki nag≥Ûwkowe i dokumentacja programisty do Xlt.

%package static
Summary:	Xlt static library
Summary(pl):	Biblioteka statyczna Xlt
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
Xlt static library.

%description static -l pl
Biblioteka statyczna Xlt.

%prep
%setup -q -n LessTifExtensions-%{version}

%build
libtoolize -c -f
aclocal
autoconf
automake -a -c
%configure \
	--enable-static \
	--enable-shared \
	--disable-build-12 \
	--disable-build-20 \
	--disable-build-21 \
	--enable-build-12

%{__make} X_EXTRA_LIBS="-lXm"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXlt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README}.gz
%attr(755,root,root) %{_libdir}/libXlt.so
%attr(755,root,root) %{_libdir}/libXlt.la
%{_includedir}/Xlt
%{_aclocaldir}/ac_find_xlt.m4
%{_aclocaldir}/ac_find_xpm.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXlt.a
