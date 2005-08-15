# $Rev: 3353 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	mkfontdir application
Summary(pl):	Aplikacja mkfontdir
Name:		xorg-app-mkfontdir
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/mkfontdir-%{version}.tar.bz2
# Source0-md5:	14bf53da1d0b8d0f47afea0a07e54989
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/mkfontdir-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
mkfontdir application.

%description -l pl
Aplikacja mkfontdir


%prep
%setup -q -n mkfontdir-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
