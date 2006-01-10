Summary:	mkfontdir application
Summary(pl):	Aplikacja mkfontdir
Name:		xorg-app-mkfontdir
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/mkfontdir-%{version}.tar.bz2
# Source0-md5:	7bf7543a2af76c5f4376fcd18a86551e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-app-mkfontscale
#BuildArch:	noarch but automake doesn't like it
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontdir application.

%description -l pl
Aplikacja mkfontdir.

%prep
%setup -q -n mkfontdir-%{version}

%build
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

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
