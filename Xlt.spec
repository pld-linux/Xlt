Summary:	The LessTif/Motif extension library
Summary(pl):	Biblioteka rozszerzeñ do LessTifa/Motifa
Name:		Xlt
Version:	9.2.9
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/xlt/%{name}-%{version}.tar.gz
# Source0-md5:	5159ced8318597b9a303c3453bbe1658
Patch0:		%{name}-am18.patch
URL:		http://xlt.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	motif-devel >= 1.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LessTif/Motif extension library. This consists of several widgets
and convience functions to make LessTif, or if you must Motif,
programming more enjoyable.

%description -l pl
Biblioteka rozszerzeñ do LessTifa/Motifa. Zawiera trochê widgetów i
funkcji ¿eby nieco uprzyjemniæ programowanie z u¿yciem LessTifa czy
Motifa.

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
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static

%{__make} \
	X_EXTRA_LIBS="-lXm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

# workaround - configure decides not to install *.m4 if aclocaldir is not writable
install ac_find_*.m4 $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libXlt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,gif}
%attr(755,root,root) %{_libdir}/libXlt.so
%{_libdir}/libXlt.la
%{_includedir}/Xlt
%{_aclocaldir}/ac_find_xlt.m4
%{_aclocaldir}/ac_find_xpm.m4
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libXlt.a
