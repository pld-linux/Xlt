
%define srcname	LessTifExtensions

Summary:	The LessTif extension library
Summary(pl):	Biblioteka rozszerzeñ do LessTifa
Name:		Xlt
Version:	9.0.9
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.lesstif.org/pub/hungry/lesstif/srcdist/%{name}-%{version}.tar.gz
BuildRequires:	lesstif-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The LessTif extension library. This consists of several widgets and
convience functions to make LessTif, or if you must Motif, programming
more enjoyable.

%description -l pl
Biblioteka rozszerzeñ do LessTifa. Zawiera trochê widgetów i funkcji
¿eby nieco uprzyjemniæ programowanie z u¿yciem LessTifa czy Motifa.

%package devel
Summary:	Xlt header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja Xlt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Xlt header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do Xlt.

%package static
Summary:	Xlt static library
Summary(pl):	Biblioteka statyczna Xlt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Xlt static library.

%description static -l pl
Biblioteka statyczna Xlt.

%prep
%setup -q -n %{srcname}-%{version}

%build
libtoolize -c -f
aclocal
autoconf
automake -a -c
%configure \
	--enable-static \
	--enable-shared \
	--enable-build-12 \
	--enable-default-12 \
	--disable-build-20 \
	--disable-default-20

%{__make} X_EXTRA_LIBS="-lXm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
